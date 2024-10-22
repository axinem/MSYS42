from django.urls import path
from . import views

urlpatterns = [
    path('', views.openpos_view, name='openpos'),
    path('item_list.html/', views.item_list_view, name='item_list'),
    path('item_form/', views.item_form, name='item_form'),
    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'), 
    path('orders/new/', views.create_order, name='create_order'),  
    path('orders/new/', views.openpos_view, name='open_pos'),
    path('orders/<int:order_id>/', views.view_order, name='view_order'), 
    path('orders/<int:order_id>/add_items/', views.add_items_to_order, name='add_items_to_order'),  
    path('orders/<int:order_id>/delete_item/<int:item_order_id>/', views.delete_item_from_order, name='delete_item_from_order'),
]
