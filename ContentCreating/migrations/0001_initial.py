# Generated by Django 4.0.5 on 2022-12-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Your Name', max_length=60)),
                ('channelName', models.TextField(default=models.CharField(default='Your Name', max_length=60))),
                ('description', models.TextField(default='very Powerful Content')),
                ('isChannel', models.BooleanField(default=False)),
                ('logo', models.ImageField(default='ChannelLogo/default.svg', upload_to='ChannelLogo/')),
            ],
        ),
    ]