# Generated by Django 3.2 on 2021-05-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_alter_home_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home',
            new_name='Nutrition',
        ),
    ]