# Generated by Django 3.1 on 2023-12-18 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lname',
            new_name='last_name',
        ),
    ]
