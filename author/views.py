from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from  .forms import  AuthorForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
# Create your views here.
def all_authors(request):

    all_author = Author.objects.all()
    return render(request, r"author\authors.html", {'all_author' : all_author})



class AuthorCreateView(CreateView):

    template_name = 'author/Creat_author.html'
    form_class = AuthorForm
    queryset = Author.objects.all()

    def form_valid(self, form ):
        return super().form_valid(form)

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/authors'
    template_name = 'author/author-delete.html'


class AuthorUpdateView(UpdateView):
    model = Author
    template_name =  'author/Update_author.html'
    form_class = AuthorForm
