# Generated by Django 3.2.12 on 2022-07-11 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('tms_create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('tms_create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=images.models.user_directory_path)),
                ('image_mini', models.ImageField(unique=True, upload_to=images.models.user_directory_path)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='images.album')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='images.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'user')},
            },
        ),
    ]
