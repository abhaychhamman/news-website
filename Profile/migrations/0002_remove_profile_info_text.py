# Generated by Django 4.1.2 on 2022-12-14 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_info',
            name='text',
        ),
    ]
