from json import dump, load

from settings import data_directory


class Cache:

    def __init__(self):
        self.last_id = self.restore_last_id()

    @staticmethod
    def restore_last_id():
        """
        Восстанавливет ID последней отработанной темы.
        :return: None
        """
        try:
            data = open(data_directory() + 'last_id.data')
        except IOError:
            print('Внимание! Не найден файл ID темы. Будет создан новый.')
            return 0
        else:
            with data:
                return load(data)

    def save(self):
        """
        Сохраняет кеш на диск. При повторном запуске краулера кеш восстанавливается в load()
        :return: None
        """
        with open(data_directory() + 'last_id.data', 'w') as data:
            dump(self.last_id, data)
