from django import forms
from authentication.models import ROLE_CHOICES, CustomUser
from django.forms import ModelForm


class UserForm(ModelForm):
    # first_name = forms.CharField(help_text="First name")
    # middle_name = forms.CharField(help_text="First name")
    # last_name = forms.CharField(help_text="First name")
    # email = forms.CharField(help_text="First name")
    # password = forms.CharField(widget=forms.PasswordInput(),help_text="First name")
    # role = forms.ChoiceField(choices=ROLE_CHOICES)
    # is_active = forms.BooleanField()
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', "password",]
