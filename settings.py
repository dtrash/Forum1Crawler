
def data_directory() -> str:
    """
    Рабочий католог в котором краулер сохраняет результат свой работы.
    :rtype: str
    """
    # TODO нужно создавать все необходимые директории
    return 'c:/test/1CForumCrawler/'


def base_url() -> str:
    """
    Неизменяемая часть адреса для получения данных.
    :rtype: str
    """
    return 'https://partners.v8.1c.ru/forum/topic/'


def login_url() -> str:
    """
    Ссылка на страницу авторизации.
    :rtype: str
    """
    return 'https://login.1c.ru/login'


def crawl_start_id() -> int:
    """
    Идентификатор темы с которой начнется загрузка сообщений, если это первый запуск программы.
    :rtype: int
    """
    return 225_047


def max_attempts() -> int:
    """
    Максимальное количество попыток получения данных. Если за указанное число попыток не будет
    получена новая порция данных, то программа закончит свою работу.
    :rtype: int
    """
    return 50


def sleep_timer() -> float:
    """
    Время ожидания, в секундах, между обращениями к серверу.
    В идеале брать из robots.txt, но сейчас не разумно тратить время на парсинг робота.
    :rtype: float
    """
    return 1.0


def no_page_found() -> str:
    """
    Текст сообщения который возвращает форум если сообщение с указанным id не найдено.
    :rtype: str
    """
    return 'Такой страницы нет.'


def no_next_page_found() -> str:
    """
    Текст сообщения который возвращает форум если страницы с указанным id не найдено.
    :rtype: str
    """
    return "Пока еще нет такой страницы в этой теме."


def cons_score_filter() -> int:
    """
    Граница, ничиная с которой сообщение считается негативным.
    :return: число.
    """
    return -10


def pros_score_filter() -> int:
    """
    Граница, ничиная с которой сообщение считается позитивным.
    :return: число.
    """
    return 10