from django.urls import path

from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("book_list/", views.books_list, name="list"),
    path("upload_book/", views.upload_book, name="upload"),
    path("book_list/<int:pk>/", views.delete_book, name="delete"),
    path("book_list/connect/<int:pk>/", views.connect, name="connect"),
    path("class/book_list/", views.BookListView.as_view(), name="class_list"),
    path("class/upload_book/", views.UploadBookView.as_view(), name="class_upload"),
]
