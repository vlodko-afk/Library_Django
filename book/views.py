from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
# Create your views here.

def all_books(request):
    # all = [Book().get_all()[i].to_dict() for i in range(len(Book().get_all()))]
    # all_book = [Book().get_all()[i].to_dict() for i in range(len(Book().get_all()))]
    all_book = Book.objects.all()
    # return HttpResponse(all_book)
    return render(request, r'news\book.html', {'all_book': all_book})


class BookCreateView(CreateView):

    template_name = 'news\Creat_books.html'
    form_class = BookForm
    queryset = Book.objects.all()

    def form_valid(self, form ):
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            return super().form_valid(form)
        else:
            form = form.cleaned_data()
            return super().form_valid(form)



# def BookCreateView(request):
#     error = ''
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Книжку створено не правильно'
#     form = BookForm()
#     data = {
#         'form': form,
#         'error': error,
#     }
#     return render(request, 'news\Creat_books.html', data)
#     return HttpResponse(Book().create(name="testBook", description="testDescription"))


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books'
    template_name = 'news/book-delete.html'
# def delete_book_by_id(request, id):
#     return  HttpResponse(Book().delete_by_id(id))


class BookUpdateView(UpdateView):
    model = Book
    template_name =  'news/Update_book.html'
    form_class = BookForm
# def update_book_by_id(request):
#     pass
