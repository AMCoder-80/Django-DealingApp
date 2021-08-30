from django import forms
from .models import Property


class PropertyCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyCreationForm, self).__init__(*args, **kwargs)
        self.fields['options'].required = False

    class Meta:
        model = Property
        exclude = ['created']