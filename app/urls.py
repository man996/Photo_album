from django.contrib import admin
from django.urls import path, include

from images.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/images/', ImagesAPIView.as_view()),
    path('api/v1/album/', AlbumAPIView.as_view()),
    path('api/v1/images/list/', ImagesList.as_view()),
    path('api/v1/album/list/', AlbumList.as_view()),
    path('api/v1/images/delete/', ImagesDelete.as_view()),
    path('api/v1/album/delete/', AlbumDelete.as_view()),
    path('api/v1/images/retrieveupdatedestroy/', ImagesRetrieveUpdateDestroy.as_view()),
    path('api/v1/album/retrieveupdatedestroy/', AlbumRetrieveUpdateDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
