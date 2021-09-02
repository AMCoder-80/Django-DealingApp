from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, ListView
from .forms import DealerCreationForm, SignInForm, ProfileForm
from .models import *
from property.models import Property
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SignIn(LoginView):
    template_name = 'account/login.html'
    form_class = SignInForm
    redirect_authenticated_user = True


class SignOut(LoginRequiredMixin, LogoutView):
    pass


class Dashboard(LoginRequiredMixin, ListView):
    model = Property
    context_object_name = 'properties'
    template_name = 'AdminLTE/dashboard.html'


class UserCreation(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('account:user_creation')
    model = User
    fields = '__all__'
    template_name = 'account/user_creation.html'


class DealerCreation(CreateView):
    success_url = reverse_lazy('account:user_creation')
    model = Dealer
    form_class = DealerCreationForm
    template_name = 'account/registration.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Dealer
    form_class = ProfileForm
    template_name = 'AdminLTE/profile.html'

    def get_object(self, queryset=None):
        user = Dealer.objects.get(pk=self.request.user.pk)
        return user

    def get_success_url(self):
        return reverse('account:profile')


def test(request):
    return render(request, 'deal_app/detail.html')