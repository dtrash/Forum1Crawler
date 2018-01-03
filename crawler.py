
from time import sleep

import requests
from colorama import Fore

from my_parser import MyParser
from cache import Cache
from file_io_driver import FileIODriver
from secret import authorization_data
from settings import base_url, no_page_found, sleep_timer, max_attempts, login_url, no_next_page_found, \
    crawl_start_id


class Crawler:

    def __init__(self):
        self.parser = MyParser()
        self.__base_url = base_url()
        self.__login_url = login_url()
        self.__failures = 0
        self.__session = self.open_session()
        self.cache = Cache()
        self.file_io_driver = FileIODriver()
        self.next_url_id = int(self.cache.last_id) + 1 if self.cache.last_id else crawl_start_id()

    def break_data_load(self) -> bool:
        return True if self.__failures == max_attempts() else False

    def open_session(self):
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0'
        })

        auth_data = authorization_data()
        page = session.get(self.__login_url).text
        auth_data['execution'] = self.parser.execution_data(page)
        session.post(self.__login_url, data=auth_data)

        return session

    def load_topic(self, page, full_url):
        self.next_url_id = self.parser.next_url_id(page)
        page_index = 1
        while True:
            self.parser.parse_page(page)
            self.file_io_driver.save_messages(self.parser)
            next_page_url_of_same_topic = full_url.replace('page=0', 'page=' + str(page_index))
            page = self.__session.get(next_page_url_of_same_topic)
            if no_next_page_found() in page.text:
                break
            else:
                print(Fore.BLUE + 'Найдена новая страница темы')
            page_index += 1

    def load_data(self):
        while self.next_url_id:
            # page=0 - первая страница темы, pageSize=Size5 - 50 сообщений на странице, максимальная порция.
            full_url = self.__base_url + str(self.next_url_id) + '?page=0&pageSize=Size5'
            self.cache.last_id = self.next_url_id
            page = self.__session.get(full_url)
            if no_page_found() in page.text:
                print(Fore.RED + 'Страница не найдена')
                self.__failures += 1
                # Странная ситуация, битых ссылок в этом алгоритме быть не должно. Но если попали на такую ссылку,
                # то ищем следующую рабочую перебором.
                self.next_url_id += 1
                sleep(sleep_timer())
            else:
                print(Fore.WHITE + 'Скачана страница -->', Fore.GREEN + str(self.next_url_id))
                self.load_topic(page, full_url)
                self.__failures = 0
                self.cache.last_id = self.next_url_id
            if self.break_data_load():
                print(Fore.YELLOW + 'Достигнуто максимальное количество попыток. Работа завершена id',
                      str(self.next_url_id))
                break
        else:
            print(Fore.GREEN + 'Работа успешно завершена')

    def save_data(self):
        self.cache.save()
        self.file_io_driver.save_messages(self.parser)
        self.file_io_driver.close_files()
