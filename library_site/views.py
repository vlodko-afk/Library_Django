from django.shortcuts import render
import sys
from book import models


def index(request):
    books = models.Book.objects.all()
    return render(request, r'index.html', {'books': books})