# Generated by Django 5.0.2 on 2024-03-12 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_visastatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('job_application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.jobapplication')),
            ],
        ),
    ]
