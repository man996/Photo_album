from django.test import TestCase
from rest_framework.test import APITestCase
import mock
from django.core.files import File
from django.contrib.auth.models import User


# Create your tests here.
from images.models import Album


class PhotoAlbumTests(APITestCase):

    def setUP(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'photo.jpg'

        user_test1 = User.objects.create_user(username='test', password='1q2w3e')
        user_test1.save()
        user_test2 = User.objects.create_user(username='test2', password='1q2w3e5t6y7u')
        user_test2.save()

        self.one_album = Album.objects.create(
            name='test_album',
            title='for tests',
            id=10,
            user=user_test1,
        )
