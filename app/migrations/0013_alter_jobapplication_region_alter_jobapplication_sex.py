# Generated by Django 5.0.2 on 2024-03-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_jobapplication_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='region',
            field=models.CharField(choices=[('addis_ababa', 'Addis Ababa'), ('oromia', 'Oromia'), ('amhara', 'Amhara'), ('tigray', 'Tigray'), ('south', 'South'), ('somali', 'Somali'), ('afar', 'Afar'), ('benishangul', 'Benishangul Gumuz'), ('gambella', 'Gambella'), ('harar', 'Harar')], default='Addis Ababa', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]