# Generated by Django 3.1.7 on 2021-11-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=16, unique=True)),
                ('qr_code', models.ImageField(upload_to='')),
                ('point', models.SmallIntegerField()),
                ('serial_no', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('expiry', models.DateField()),
                ('dealer_benifit', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
