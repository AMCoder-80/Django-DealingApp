from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)
from .models import Property
from .forms import PropertyCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .decorators import anonymous_only
# Create your views here.


class Home(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'deal_app/home.html'
    context_object_name = 'homes'
    

class PropertyCreation(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyCreationForm
    success_url = reverse_lazy('account:profile')
    template_name = 'AdminLTE/Create_Update.html'


class PropertyDetail(DetailView):
    ...


class PropertyDelete(DeleteView):
    ...


class PropertyUpdate(UpdateView):
    ...


@anonymous_only('property:home')
def greeting(request):
    return render(request, 'deal_app/greeting.html')
