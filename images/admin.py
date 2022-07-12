from django.contrib import admin

# Register your models here.
from images.models import *

admin.site.register(Images)

admin.site.register(Album)
