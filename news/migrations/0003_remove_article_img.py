# Generated by Django 4.1.1 on 2022-09-06 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
    ]