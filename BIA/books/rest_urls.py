from django.urls import path
import books.rest_views as rest_views

urlpatterns = [
    path('books_crud/', rest_views.BookView.as_view(), name='books-crud'),
    path('books_crud/<int:book_id>/', rest_views.BookView.as_view(), name='modify-books-crud'),

]