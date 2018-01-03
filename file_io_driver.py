import csv
import os

import settings
from forum_message import ForumMessage


class FileIODriver:
    """
    Структура каталога data/*
    pros.csv - сообщения с положительной оценкой (по-умолчанию +10 и выше)
        * datetime - время и дата сообщения,
        * category - раздел форума,
        * total_score - итоговый рейтинг сообщения: положительный рейтинг + отрицательный рейтинг,
        * pros_score - положительный рейтинг,
        * cons_score - отрицательный рейтинг,
        * url - ссылка на сообщение,
        * username - имя пользователя,
        * company - компания в которой работает пользователь,
        * text - текст сообщения.
    cons.csv - сообщения с отрицательной оценкой (по-умолчанию -10 и ниже)
        структура файла совпадает с pros.csv.
    untagged.csv - не оценные сообщения, рейтинг сообщения в диапазоне [-9, 9]
        * datetime - время и дата сообщения,
        * category - раздел форума,
        * url - ссылка на сообщение,
        * username - имя пользователя,
        * company - компания в которой работает пользователь,
        * text - текст сообщения.
    """
    def __init__(self):
        self.pros_file = self.open_file('pros')
        self.cons_file = self.open_file('cons')
        self.untagged_file = self.open_file('untagged')

    def save_messages(self, parser):
        # TODO все же файлы лучше открывать непосредственно перед записью и после записи закрывать,
        # а не держать открытыми всю работу программы.
        writer_pros = csv.DictWriter(self.pros_file, fieldnames=FileIODriver.fieldnames('pros'))
        writer_cons = csv.DictWriter(self.cons_file, fieldnames=FileIODriver.fieldnames('cons'))
        writer_untagged = csv.DictWriter(self.untagged_file, fieldnames=FileIODriver.fieldnames('untagged'))
        for message in parser.messages:
            if message.total_score >= settings.pros_score_filter():
                writer_pros.writerow(message.message_representation('pros'))
            elif message.total_score <= settings.cons_score_filter():
                writer_cons.writerow(message.message_representation('cons'))
            else:
                writer_untagged.writerow(message.message_representation('untagged'))

    def close_files(self):
        self.pros_file.close()
        self.cons_file.close()
        self.untagged_file.close()

    @staticmethod
    def open_file(file_type):
        file_map = FileIODriver.file_map()
        file_path = file_map[file_type]
        if not os.path.isfile(file_path):
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = FileIODriver.fieldnames(file_type)
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        return open(file_path, 'a', encoding='utf-8')

    @classmethod
    def file_map(cls):
        return {
            'pros': settings.data_directory() + 'data/pros.csv',
            'cons': settings.data_directory() + 'data/cons.csv',
            'untagged': settings.data_directory() + 'data/untagged.csv'
        }

    @staticmethod
    def fieldnames(file_type):
        if file_type == 'untagged':
            return ForumMessage.fieldnames_untagged_message()
        else:
            return ForumMessage.fieldnames_pros_or_cons_message()