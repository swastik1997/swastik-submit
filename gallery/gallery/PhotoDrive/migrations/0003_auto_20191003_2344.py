# Generated by Django 2.2.6 on 2019-10-03 23:44

import PhotoDrive.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoDrive', '0002_auto_20191003_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='directory',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_album', to='PhotoDrive.Album'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
    ]
