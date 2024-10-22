from django.urls import path
from django.contrib import admin
from . import views
from .views import product_list, ProductDetailView, add_to_cart

urlpatterns=[
    path('', views.base, name='infotemp'),
    path('infotemp/', views.base, name='infotemp'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('admin/', admin.site.urls),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart')
]