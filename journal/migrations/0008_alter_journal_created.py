# Generated by Django 3.2.4 on 2021-06-23 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_alter_journal_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
