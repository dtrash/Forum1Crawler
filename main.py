from colorama import init

from crawler import Crawler


def save_data(crawler):
    crawler.save_data()


def main():
    """
    Грабит данные с https://partners.v8.1c.ru/forum и сохраняет в директорию
    указанную в settings.py get_data_directory() для последующего построения модели анализа тональности.
    Для работы краулера нужно создать файл secret.py в котором реализовать функцию get_authorization_data()
    возвращающую словарь с ключами: username и password. Значения ключей - логин и пароль для доступа к форуму.

    Необходимо самостоятельно создать модуль secret.py и разместить в нем функцию:
    def authorization_data():
    return {
        'inviteCode': '',
        'username': '', # Логин на форуме
        'password': '', # Пароль на форуме
        '_eventId': 'submit',
        'geolocation': '',
        'submit': 'Войти',
        'rememberMe': 'on'
    }

    Используемые сторонние библиотеки:
        * requests
        * beautifulsoup4
        * colorama

    """
    init()

    crawler = Crawler()

    try:
        crawler.load_data()

    except KeyboardInterrupt:
        save_data(crawler)

    else:
        save_data(crawler)


if __name__ == '__main__':
    main()
