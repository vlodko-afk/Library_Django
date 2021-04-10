from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_authors, name='authors'),
    # path('<int:id>', views.author_by_id, name='author_by_id'),
    # path('<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('create/', views.AuthorCreateView.as_view(), name='create_author'),
    # path('delete/<int:id>', views.delete_author_by_id, name='delete_author_by_id'),
    # path('update/<int:id>', views.update_author_by_id, name='update_author_by_id'),
    path('<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('<int:pk>/update', views.AuthorUpdateView.as_view(), name='author-update'),
]
