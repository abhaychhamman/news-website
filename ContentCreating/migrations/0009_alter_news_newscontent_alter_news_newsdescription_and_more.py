# Generated by Django 4.0.5 on 2022-12-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContentCreating', '0008_jokes_news_quotes_alter_memes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsContent',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsDescription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsTitle',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='userQuotes',
            field=models.CharField(default='', max_length=700),
        ),
    ]
