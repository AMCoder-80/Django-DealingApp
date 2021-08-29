from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import DealerCreationForm, SignInForm
from .models import *

# Create your views here.


class SignIn(LoginView):
    template_name = 'account/login.html'
    form_class = SignInForm
    redirect_authenticated_user = True


class SignOut(LogoutView):
    pass


class UserCreation(CreateView):
    success_url = reverse_lazy('account:user_creation')
    model = User
    fields = '__all__'
    template_name = 'account/user_creation.html'


class DealerCreation(CreateView):
    success_url = reverse_lazy('account:user_creation')
    model = Dealer
    form_class = DealerCreationForm
    template_name = 'account/registration.html'


def test(request):
    return render(request, 'deal_app/greeting.html')