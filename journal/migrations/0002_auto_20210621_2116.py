# Generated by Django 3.2.4 on 2021-06-21 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='journal',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Journals'},
        ),
    ]
