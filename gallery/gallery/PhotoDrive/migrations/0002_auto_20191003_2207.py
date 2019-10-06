# Generated by Django 2.2.6 on 2019-10-03 22:07

import PhotoDrive.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoDrive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
        migrations.AlterField(
            model_name='album',
            name='directory',
            field=models.FileField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
    ]