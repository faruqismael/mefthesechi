# Generated by Django 4.2.6 on 2024-02-19 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banner',
            new_name='CarouselSlide',
        ),
    ]
