# Generated by Django 4.1 on 2022-12-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_projectwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectwork',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]