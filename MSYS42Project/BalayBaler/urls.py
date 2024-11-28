from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from .views import add_to_cart, cart_view, process_order, thankyou

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info_view, name='info'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('admin/', admin.site.urls),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
    path('thankyou/', thankyou, name='thankyou'),
    path('payment/', views.payment, name='payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

