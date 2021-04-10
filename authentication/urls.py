from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),
    path('<int:user_id>', views.user_by_id, name='user_by_id'),
    path('create/', views.create_update_user, name='create_user'),
    path('delete/<int:user_id>', views.delete_user_by_id, name='delete_user_by_id'),
    path('update/<int:user_id>', views.create_update_user, name='update_user_by_id'),
]
