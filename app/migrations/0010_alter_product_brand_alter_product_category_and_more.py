# Generated by Django 4.0.3 on 2022-03-15 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_brand_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.sub_category'),
        ),
    ]
