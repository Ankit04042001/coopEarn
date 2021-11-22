
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('coupons/',views.CouponListView.as_view(), name='coupon_list'),
    path('book/<int:pk>',views.CouponDetailView.as_view(), name='coupon'),
    path('use_coupon/',views.use_coupon, name='use_coupon'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)