from django import forms
from django.forms import SelectDateWidget

from authentication.models import CustomUser
from book.models import Book


class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class BookChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name}"

class OrderForm(forms.Form):
    user = UserChoiceField(queryset=CustomUser.objects.all())
    book = BookChoiceField(queryset=Book.objects.all())
    plated_end_at = forms.DateField(widget=SelectDateWidget())
