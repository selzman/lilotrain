# Generated by Django 4.2.3 on 2023-07-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
