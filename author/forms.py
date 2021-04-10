from .models import Author
from django.forms import ModelForm, TextInput, Textarea


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic',  ]

        # widgets = {
        #      'name': TextInput(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'Назва автора'
        #      }),
        #      'surname': TextInput(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'Прізвище автора'
        #      }),
        #      'patronymic': TextInput(attrs = {
        #         'class': 'form-control',
        #         'placeholder':  'По батькові'
        #      }),
        # }
