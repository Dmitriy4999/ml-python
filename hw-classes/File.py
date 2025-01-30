from datetime import datetime


class File:

    def __init__(self, name: str, size: int, date: datetime, owner: str):
        self.name = name
        self.size = size
        self.date = date
        self.owner = owner

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.size}, {self.date}, {self.owner})'

    def save(self, path: str):
        # сохранить файл
        print(f'Saving file {self} to {path.replace(path[0], "", 1)}')

    def update(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'date' in kwargs:
            self.date = kwargs['date']
        if 'owner' in kwargs:
            self.owner = kwargs['owner']

    def delete(self):
        # удалить любой тип файла
        print(f'Deleting file {self}')
