# Generated by Django 2.2.6 on 2022-05-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20220512_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
            ],
        ),
    ]
