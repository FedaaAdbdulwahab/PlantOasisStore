# Generated by Django 3.1 on 2023-12-18 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='OrderForm',
        ),
    ]