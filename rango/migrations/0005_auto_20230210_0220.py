# Generated by Django 2.2.28 on 2023-02-10 02:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0004_auto_20230209_2319'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfiles',
            new_name='UserProfile',
        ),
    ]
