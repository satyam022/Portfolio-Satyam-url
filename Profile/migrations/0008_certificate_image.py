# Generated by Django 4.1 on 2022-12-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_rename_work_experiencework'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
