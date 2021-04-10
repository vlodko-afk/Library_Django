from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_orders, name='orders'),
    path('<int:order_id>', views.order_by_id, name='order_by_id'),
    path('create/', views.create_update_order, name='create_order'),
    path('delete/<int:order_id>', views.delete_order_by_id, name='delete_order_by_id'),
    path('update/<int:order_id>', views.create_update_order, name='update_order_by_id'),
]