from django import forms
from .models import Glasses, Client


class GlassesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GlassesForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Glasses
        exclude = ['colorFrame', ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'address', 'email']