from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.list_or_create_orders, name='list-or-create-orders'),
    path('orders/<int:order_id>/', views.retrieve_update_or_delete_order, name='retrieve-update-or-delete-order'),
    path('orders/<int:order_id>/items/', views.list_or_create_order_items, name='list-or-create-order-items'),
    path('orders/<int:order_id>/items/<int:item_id>/', views.retrieve_update_or_delete_order_item, name='retrieve-update-or-delete-order-item'),
]
