from django.db import models

# Create your models here.


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=16,unique=True)
    qr_code = models.ImageField(upload_to='qrcode', null=True, blank=True)
    point = models.SmallIntegerField()
    serial_no = models.IntegerField()
    product_name = models.CharField(max_length=50)
    denomination = models.CharField(max_length=50, blank=True, null=True)
    expiry = models.DateField()
    dealer_benifit = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, default="Not Used")

    def __str__(self):
        return str(self.coupon_code)
