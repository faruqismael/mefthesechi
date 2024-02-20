# Generated by Django 4.2.6 on 2024-02-19 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('alt_text', models.CharField(blank=True, help_text='Alternative text for image', max_length=255)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.about')),
            ],
        ),
    ]
