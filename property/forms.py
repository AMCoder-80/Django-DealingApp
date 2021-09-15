from django import forms

from .models import Property
from account.models import User


class PropertyCreationForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PropertyCreationForm, self).__init__(*args, **kwargs)
        self.fields['options'].required = False
        self.fields['date_built'].label += " (25-10-1399)"
        self.user = user
        self.fields['owner'].queryset = User.objects.filter(dealer=user, status='O')

    class Meta:
        model = Property
        exclude = ['created', 'image']


class PropertyImageForm(forms.Form):
    images = forms.ImageField(label='تصاویر', widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PropertyRequestUpdate(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PropertyRequestUpdate, self).__init__(*args, **kwargs)

        # In this way, you can specify the query set for each relational field
        self.fields['requesters'].queryset = User.objects.filter(status='B', dealer=user)

    class Meta:
        model = Property
        fields = ['requesters', ]
