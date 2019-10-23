# Generated by Django 2.2.6 on 2019-10-21 12:22

import PhotoDrive.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoDrive', '0008_auto_20191021_0301'),
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