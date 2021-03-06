# Generated by Django 3.2 on 2021-04-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210417_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
