# Generated by Django 3.2 on 2021-05-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_rename_home_nutrition'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nutrition',
            new_name='Nutritious',
        ),
    ]
