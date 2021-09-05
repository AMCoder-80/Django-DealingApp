from django import forms

from .models import Property


class PropertyCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyCreationForm, self).__init__(*args, **kwargs)
        self.fields['options'].required = False

        self.fields['date_built'].label += " (25-10-1399)"


    class Meta:
        model = Property
        exclude = ['created', 'image']


class PropertyImageForm(forms.Form):
    images = forms.ImageField(label='تصاویر', widget=forms.ClearableFileInput(attrs={'multiple': True}))