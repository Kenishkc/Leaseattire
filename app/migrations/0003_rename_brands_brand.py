# Generated by Django 4.0.3 on 2022-03-15 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_brands'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='Brand',
        ),
    ]