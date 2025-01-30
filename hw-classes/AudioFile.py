from datetime import datetime

from File import File


class AudioFile(File):

    def __init__(self, name: str, size: int, date: datetime, owner: str, bitrate: int, length: int):
        super().__init__(name, size, date, owner)
        self.bitrate = bitrate
        self.length = length

    def __str__(self):
        return (f'{self.__class__.__name__}({self.name}, {self.size}, {self.date}, '
                f'{self.owner}, {self.length})')

    def save(self, path: str):
        # сохранить аудио-файл
        print(f'Saving audio-file {self} to {path.replace(path[0], "", 1)}')

    def update(self, **kwargs):
        super().update(**kwargs)
        if 'bitrate' in kwargs:
            self.bitrate = kwargs['bitrate']
        if 'length' in kwargs:
            self.length = kwargs['length']
