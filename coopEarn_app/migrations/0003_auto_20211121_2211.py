# Generated by Django 3.1.7 on 2021-11-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coopEarn_app', '0002_remove_coupon_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='status',
            field=models.CharField(default='active', max_length=20),
        ),
    ]