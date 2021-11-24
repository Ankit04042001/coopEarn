from django.contrib.messages.api import error
from django.http.response import HttpResponse
from django.shortcuts import render
import uuid
from .models import Coupon
from django.views import generic
from django.contrib import messages
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime


# Create your views here.


def index(request):
    if(request.method == 'POST'):
        pointCoupon = request.POST.get('pointCoupon')
        serialNo = request.POST.get('serialNo')
        productName = request.POST.get('productName')
        denomination = request.POST.get('denomination')
        quantity = request.POST.get('quantity')
        expiry = request.POST.get('expiry')
        dealerBenifit = request.POST.get('dealerBenifit')

        counter = int(quantity)
        for count in range(0,counter):
            coupon_code = str(uuid.uuid4().hex)[0:16]
            alreadyExist = Coupon.objects.all().filter(coupon_code = coupon_code)
            while len(alreadyExist) > 0:
                coupon_code = str(uuid.uuid4().hex)[0:16]
                alreadyExist = Coupon.objects.all().filter(coupon_code = coupon_code)
            qrcode_img = qrcode.make(coupon_code)
            canvas = Image.new('RGB',(330,330), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            fname = f'qr_code-{coupon_code}.png'
            buffer = BytesIO()            
            canvas.save(buffer,'PNG')
            coupon = Coupon(coupon_code = coupon_code, point = pointCoupon, serial_no = serialNo, product_name = productName, denomination = denomination, expiry = expiry, dealer_benifit = dealerBenifit)
            coupon.qr_code = ImageFile(SimpleUploadedFile(name=fname, content=buffer.getvalue(), content_type='image/png'))
            coupon.save()
        
    return render(request, 'index.html')


class CouponListView(generic.ListView):
    model = Coupon
    template_name = 'coupon_list.html'
    context_object_name = 'coupon_list'
    


class CouponDetailView(generic.DetailView):
    model = Coupon
    template_name = 'coupon_detail.html'
    context_object_name = 'coupon'


def use_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon')
        get_coupon = Coupon.objects.get(coupon_code = coupon_code)
        print(get_coupon)
        print(get_coupon.expiry < datetime.date.today())
        try:
            get_coupon = Coupon.objects.get(coupon_code = coupon_code)
            if get_coupon.expiry > datetime.date.today():
                if get_coupon.status == "Not Used":
                    get_coupon.status = "Used"
                    get_coupon.save()
                    messages.success(request, "Coupon accepted")
                else:
                    messages.error(request, "Coupon already used")
            else:
                messages.error(request, "Coupon Expired")
        except:
            print(error)
            messages.error(request, "Invalid Coupon")
        
    return render(request,'use_coupon.html')

