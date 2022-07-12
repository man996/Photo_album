import os
import uuid
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return [os.path.join(f'media/{instance.user}', filename), ext]


# def thumbnail_pic(path):
#     ext = path.split('.')[-1]
#     # glob.glob (pathname), возвращает список всех подходящих путей к файлам
#     if ext in ('jpg', 'jpeg'):
#         a=glob.glob(r'./img/*.jpg')
#         for x in a:
#             name = os.path.join(path, x)
#             im = Image.open(name)
#             im.thumbnail((150, 150))
#             im.save(name, 'JPEG')
#     elif ext=='png':
#         a = glob.glob(r'./img/*.png')
#         for x in a:
#             name = os.path.join(path, x)
#             im = Image.open(name)
#             im.thumbnail((150, 150))
#             im.save(name, 'PNG')


class Album(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    tms_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=250)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'user')


class Images(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    tms_create = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    tags = models.TextField(max_length=400)

    class Meta:
        unique_together = ('name', 'user')


