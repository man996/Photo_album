import io
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
import mock
from django.core.files import File
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from images.models import Album


class PhotoAlbumTests(APITestCase):

    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'photo.jpg'

        user_test1 = User.objects.create_user(username='test', password='1q2w3e', email='Man1999@mail.ru')
        user_test1.save()
        user_test2 = User.objects.create_user(username='test2', password='1q2w3e5t6y7u', email='Man1996@mail.ru')
        user_test2.save()

        self.one_album = Album.objects.create(
            name='test_album',
            title='for tests',
            id=10,
            user=user_test1,
        )

        image = io.BytesIO()
        Image.new('RGB', (1152, 2048)).save(image, 'JPEG')
        image.seek(0)
        image_file = SimpleUploadedFile('image2.jpg', image.getvalue())

        self.data = {
            "id": 25,
            "album": 10,
            "name": 'test',
            "image": image_file,
            "tags": '#testtttt',
            'user': 1
        }
        print(user_test1)
        self.user_test1_token = Token.objects.create(user=user_test1)
        print(user_test2)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_create_valid_album(self):
        print(self)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test2_token.key)
        response = self.client.post(reverse('new_album'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_enter_valid_album(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(
            reverse('new_album', kwargs={"pk": self.one_album.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)