from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Dealer


class DealerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(DealerCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False

    class Meta:
        model = Dealer
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False
