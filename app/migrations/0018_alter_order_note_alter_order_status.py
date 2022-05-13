# Generated by Django 4.0.3 on 2022-05-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PND', 'Pending'), ('ACP', 'Accept'), ('DLV', 'Deliver'), ('CMP', 'Sucess')], max_length=10),
        ),
    ]
