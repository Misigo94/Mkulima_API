# Generated by Django 4.0.5 on 2022-07-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mkulimapp', '0004_user_image_user_location_user_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
