# Generated by Django 4.1 on 2022-12-27 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_aboutprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='date',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='title',
        ),
    ]