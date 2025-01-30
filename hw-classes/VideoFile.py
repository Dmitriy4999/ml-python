from datetime import datetime

from PhotoFile import PhotoFile


class VideoFile(PhotoFile):

    def __init__(self, name: str, size: int, date: datetime, owner: str, frame_x: int, frame_y: int, length: int):
        super().__init__(name, size, date, owner, frame_x, frame_y)
        self.length = length

    def __str__(self):
        return (f'{self.__class__.__name__}({self.name}, {self.size}, {self.date}, '
                f'{self.owner}, {self.frame_x}, {self.frame_y}, {self.length})')

    def save(self, path: str):
        # сохранить видео-файл
        print(f'Saving video-file {self} to {path.replace(path[0], "", 1)}')

    def update(self, **kwargs):
        super().update(**kwargs)
        if 'length' in kwargs:
            self.length = kwargs['length']
