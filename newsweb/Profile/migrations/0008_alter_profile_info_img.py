# Generated by Django 4.0.5 on 2022-12-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_alter_profile_info_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_info',
            name='img',
            field=models.ImageField(default='', upload_to='User/ProfileImage/'),
        ),
    ]