# Generated by Django 4.1 on 2022-12-28 11:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0016_blogpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
