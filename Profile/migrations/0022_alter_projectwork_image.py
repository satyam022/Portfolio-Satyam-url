# Generated by Django 4.1 on 2022-12-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0021_aboutprofile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectwork',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/projectwork'),
        ),
    ]
