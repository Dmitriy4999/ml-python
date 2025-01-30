from datetime import datetime

from AudioFile import AudioFile
from File import File
from PhotoFile import PhotoFile
from VideoFile import VideoFile

file = File("TextFile", 30, datetime.now(), "Dmitriy")
audio = AudioFile("Audio", 24, datetime.now(), "Dmitriy", 30000, 300)
photo = PhotoFile("Photo", 56, datetime.now(), "Dmitriy", 1024, 720)
video = VideoFile("Video", 123, datetime.now(),
                  "Vladislav", 1920, 1080, 400)

print(f'\n{file}\n{audio}\n{photo}\n{video}\n')

file.save("/remote")
audio.save("/cloud")
photo.save("/s3")
video.save("/local")

file.update(name="EditedTextFile", size=10)
audio.update(name="EditedAudio", bitrate=24000)
photo.update(name="EditedPhoto", frame_y=670)
video.update(name="EditedVideo", length=519)
print(f'\n{file}\n{audio}\n{photo}\n{video}\n')

file.delete()
audio.delete()
photo.delete()
video.delete()
