from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)

from .decorators import anonymous_only
from .forms import PropertyCreationForm, PropertyImageForm
from .models import Property, PropertyImages


# Create your views here.


class Home(LoginRequiredMixin, ListView):
    model = Property
    paginate_by = 4
    template_name = 'deal_app/home.html'
    context_object_name = 'homes'


class PropertyCreation(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyCreationForm
    success_url = reverse_lazy('account:dashboard')
    template_name = 'AdminLTE/Create_Update.html'

    def get_context_data(self, **kwargs):
        context = super(PropertyCreation, self).get_context_data(**kwargs)
        context['image_form'] = PropertyImageForm()
        return context

    def form_valid(self, form):
        result = super(PropertyCreation, self).form_valid(form)
        images = self.request.FILES.getlist('images')
        for image in images:
            PropertyImages.objects.create(property=self.object, image=image)
        return result


class PropertyDetail(DetailView):
    model = Property
    template_name = 'deal_app/detail.html'
    context_object_name = 'property'


class PropertyDelete(DeleteView):
    ...


class PropertyUpdate(UpdateView):
    model = Property
    form_class = PropertyCreationForm
    success_url = reverse_lazy('account:dashboard')
    template_name = 'AdminLTE/Create_Update.html'

    def get_context_data(self, **kwargs):
        context = super(PropertyUpdate, self).get_context_data(**kwargs)
        context['image_form'] = PropertyImageForm()
        return context

    def form_valid(self, form):
        result = super(PropertyUpdate, self).form_valid(form)
        images = self.request.FILES.getlist('images')
        print(images)
        PropertyImages.objects.filter(property=self.object).delete()
        for image in images:
            prop = PropertyImages.objects.create(property=self.object, image=image)
        return result


@anonymous_only('property:home')
def greeting(request):
    return render(request, 'deal_app/greeting.html')
