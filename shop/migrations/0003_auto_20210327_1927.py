# Generated by Django 3.1.6 on 2021-03-27 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210327_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
    ]
