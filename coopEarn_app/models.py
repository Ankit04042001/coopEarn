from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=16,unique=True)
    qr_code = models.ImageField(upload_to='pics')
    point = models.SmallIntegerField()
    serial_no = models.IntegerField()
    product_name = models.CharField(max_length=50)
    denomination = models.CharField(max_length=50, blank=True, null=True)
    expiry = models.DateField()
    dealer_benifit = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, default="Not Used")

    def __str__(self):
        return str(self.coupon_code)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.coupon_code)
        canvas = Image.new('RGB',(330,330), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.coupon_code}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

