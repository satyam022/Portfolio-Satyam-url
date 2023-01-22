# Generated by Django 4.1 on 2022-12-28 10:13

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0013_contactprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]