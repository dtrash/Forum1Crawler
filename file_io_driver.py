import csv
import os

import settings
from forum_message import ForumMessage


class FileIODriver:
    """
    data.csv - сообщения с положительной оценкой (по-умолчанию +10 и выше)
        * datetime - время и дата сообщения,
        * category - раздел форума,
        * total_score - итоговый рейтинг сообщения: положительный рейтинг + отрицательный рейтинг,
        * pros_score - положительный рейтинг,
        * cons_score - отрицательный рейтинг,
        * id - идентификатор сообщения,
        * url - ссылка на сообщение,
        * username - имя пользователя,
        * company - компания в которой работает пользователь,
        * text - текст сообщения.
    """
    def __init__(self):
        self.__file_path = settings.data_directory() + 'data.csv'
        self.create_file()

    def save_messages(self, parser):
        with open(self.__file_path, 'a', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FileIODriver.fieldnames())
            for message in parser.messages:
                writer.writerow(message.message_representation())

    def create_file(self):
        if not os.path.isfile(self.__file_path):
            with open(self.__file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = FileIODriver.fieldnames()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    @staticmethod
    def fieldnames():
        return ForumMessage.message_fieldnames()
