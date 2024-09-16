from django.urls import path
from . import views

urlpatterns=[
    path('infotemp', views.base, name='infotemp'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
]