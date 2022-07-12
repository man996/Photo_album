from rest_framework import serializers
from .models import Images, Album


class ImagesSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Images
        fields = ("id", "album", "name", "image", "tags", 'user')


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:

        model = Album
        fields = ("id", "name", "title", 'user')
