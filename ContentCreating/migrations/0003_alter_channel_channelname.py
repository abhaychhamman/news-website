# Generated by Django 4.0.5 on 2022-12-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentCreating', '0002_remove_channel_ischannel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channelName',
            field=models.TextField(default=''),
        ),
    ]
