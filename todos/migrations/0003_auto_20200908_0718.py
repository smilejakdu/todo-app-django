# Generated by Django 3.0.3 on 2020-09-08 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20200908_0709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='content',
        ),
    ]
