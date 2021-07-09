from django import forms
from django.forms import ModelForm
from .models import DescripcionRopa


class RopaForm(ModelForm):

    class Meta:
        model = DescripcionRopa
        fields = '__all__'