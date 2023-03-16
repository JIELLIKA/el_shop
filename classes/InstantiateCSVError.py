class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


class FileNotFoundError(InstantiateCSVError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствует файл item.csv'

    def __str__(self):
        return self.message
