from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)

from .decorators import anonymous_only
from .forms import PropertyCreationForm, PropertyImageForm, PropertyRequestUpdate
from .models import Property, PropertyImages


# Create your views here.

# The main view for listing all the properties
class Home(LoginRequiredMixin, ListView):
    paginate_by = 4
    template_name = 'deal_app/home.html'
    context_object_name = 'homes'

    def get_queryset(self):
        return Property.objects.filter(dealer=self.request.user)


# The Property creation view
class PropertyCreation(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyCreationForm
    success_url = reverse_lazy('account:dashboard')
    template_name = 'AdminLTE/Create_Update.html'

    # Add an extra field for image model to save required pictures
    def get_context_data(self, **kwargs):
        # Inherit from the parent object
        context = super(PropertyCreation, self).get_context_data(**kwargs)
        context['image_form'] = PropertyImageForm()
        return context

    def get_form_kwargs(self):
        context = super(PropertyCreation, self).get_form_kwargs()
        context.update({'user': self.request.user})
        return context

    # Since we defined an extra field, we need to save its value separately
    def form_valid(self, form):
        form.instance.dealer = self.request.user
        # Getting all the sent images as a list
        images = self.request.FILES.getlist('images')
        for image in images:
            # Save each image associate with the saved property model
            PropertyImages.objects.create(property=self.object, image=image)
        return super(PropertyCreation, self).form_valid(form)


class PropertyDetail(DetailView):
    model = Property
    template_name = 'deal_app/detail.html'
    context_object_name = 'property'


class PropertyDelete(DeleteView):
    model = Property
    context_object_name = 'property'
    success_url = reverse_lazy('account:dashboard')
    template_name = 'deal_app/delete.html'


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
            PropertyImages.objects.create(property=self.object, image=image)
        return result


# Only the requesters of a property will be updated here
class UpdateRequesters(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyRequestUpdate
    template_name = 'AdminLTE/requesters.html'

    def get_success_url(self):
        pk = self.request.GET.get('pk', None)
        if pk:
            return reverse('property:detail_property', kwargs={'pk': pk})
        return reverse('property:home')

    # Pass the user object to the forms
    def get_form_kwargs(self):
        context = super(UpdateRequesters, self).get_form_kwargs()
        context.update({'user': self.request.user})
        return context


# Custom decorator which does not allow authenticated users
@anonymous_only('property:home')
def greeting(request):
    return render(request, 'deal_app/greeting.html')
