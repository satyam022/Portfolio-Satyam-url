# Generated by Django 4.1 on 2022-12-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0014_blogpage_date_alter_blogpage_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='is_active',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
