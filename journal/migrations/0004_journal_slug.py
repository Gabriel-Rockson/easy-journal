# Generated by Django 3.2.4 on 2021-06-23 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20210622_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
