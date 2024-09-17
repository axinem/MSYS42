from django.urls import path
from . import views

urlpatterns=[
    path('', views.base, name='infotemp'),
    path('infotemp/', views.base, name='infotemp'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
]