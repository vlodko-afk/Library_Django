from .models import Book
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField
from author.models import Author

class AuthorChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} {obj.surname}"

class BookForm(ModelForm):
    # authors = AuthorChoiceField(queryset=Author.objects.all())
    class  Meta:
        model = Book
        # authors = AuthorChoiceField(queryset=Author.objects.all())
        fields = ['name', 'description', 'count', "authors"]
        # authors = AuthorChoiceField(queryset=Author.objects.all())

        # widgets = {
        #      'name': TextInput(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'Назва книги'
        #      }),
        #      'description': Textarea(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'Опис книги'
        #      }),
        #      'count': TextInput(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'Підрахунок книг'
        #      }),
        # }
