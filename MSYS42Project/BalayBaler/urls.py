from django.urls import path
from . import views

urlpatterns=[
    path('infotemp', views.base, name='infotemp'),
]