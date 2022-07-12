from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Images, Album
from .serializers import ImagesSerializer, AlbumSerializer


# Create your views here.

class ImagesAPIView(generics.CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = IsAuthenticated


class AlbumAPIView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = IsAuthenticated


class ImagesList(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = IsAuthenticated


class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = IsAuthenticated


class ImagesDelete(generics.DestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = IsAuthenticated


class AlbumDelete(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = IsAuthenticated


class ImagesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = IsAuthenticated


class AlbumRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = IsAuthenticated




