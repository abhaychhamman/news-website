# Generated by Django 4.0.5 on 2022-12-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentCreating', '0003_alter_channel_channelname'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='type',
            field=models.TextField(default='news'),
        ),
    ]
