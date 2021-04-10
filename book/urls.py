from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    # path('<int:id>', views.book_by_id, name='book_by_id'),
    # path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    # path('delete/<int:id>', views.delete_book_by_id, name='delete_book_by_id'),
    # path('update/<int:id>', views.update_book_by_id, name='update_book_by_id'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
]
