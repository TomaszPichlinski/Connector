from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import BookForm
from .models import Book


# Create your views here.
def connect(request, pk):
    if request.method == "POST":
        f1 = open("mysite/media/books/pdfs/", "w")
        file1 = request.FILES["myfile"].read()
        book = Book.objects.get(pk=pk)
        f = open("mysite" + book.pdf.url, "r")
        file2 = f.read()
        f1.write(file1)
        f1.write(file2)
        book.pdf = f1
        book.save()

        return HttpResponse(f.read(), content_type="text/plain")


def upload(request):
    return render(request, "connect/upload.html")


def books_list(request):
    books = Book.objects.all()
    return render(request, "connect/book_list.html", {"books": books})


def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = BookForm()
    return render(request, "connect/upload_book.html", {"form": form})


def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect("list")


class BookListView(ListView):
    model = Book
    template_name = "connect/class_book_list.html"
    context_object_name = "books"


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("class_list")
    template_name = "connect/class_upload_book.html"
