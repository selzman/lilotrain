# Generated by Django 4.2.3 on 2023-07-13 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_comment_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='product',
        ),
    ]
