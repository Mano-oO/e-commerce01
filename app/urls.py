from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', n1, name='index'),
    path('shop/', n2, name='shop'),
    path('checkout/', no, name='checkout'),
    path('contact/', n6, name='contact'),
    path('product-details/', n3, name='product-details'),
    
    path('shop-cart/', n7, name='shop-cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove-from-cart'),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('cart/', YourCartView.as_view(), name='cart'),

]