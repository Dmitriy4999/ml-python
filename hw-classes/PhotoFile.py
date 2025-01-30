from datetime import datetime

from File import File


class PhotoFile(File):

    def __init__(self, name: str, size: int, date: datetime, owner: str, frame_x: int, frame_y: int):
        super().__init__(name, size, date, owner)
        self.frame_x = frame_x
        self.frame_y = frame_y

    def __str__(self):
        return (f'{self.__class__.__name__}({self.name}, {self.size}, {self.date}, '
                f'{self.owner}, {self.frame_x}, {self.frame_y})')

    def save(self, path: str):
        # сохранить фото-файл
        print(f'Saving photo-file {self} to {path.replace(path[0], "", 1)}')

    def update(self, **kwargs):
        super().update(**kwargs)
        if 'frame_x' in kwargs:
            self.frame_x = kwargs['frame_x']
        if 'frame_y' in kwargs:
            self.frame_y = kwargs['frame_y']
