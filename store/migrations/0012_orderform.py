# Generated by Django 3.1 on 2023-12-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
