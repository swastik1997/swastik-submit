# Generated by Django 2.2.6 on 2019-10-21 03:01

import PhotoDrive.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoDrive', '0007_auto_20191007_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=PhotoDrive.models.upload_to),
        ),
    ]
