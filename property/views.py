from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)
from .models import Property
# Create your views here.


class Home(ListView):
    model = Property.objects.all()
    

class PropertyCreation(CreateView):
    ...


class PropertyDetail(DetailView):
    ...


class PropertyDelete(DeleteView):
    ...


class PropertyUpdate(UpdateView):
    ...


def greeting(request):
    return render(request, 'deal_app/greeting.html')
