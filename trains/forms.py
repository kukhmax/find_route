from django import forms

from trains.models import Train
from cities.models import City

class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Train', widget=forms.TextInput(attrs={
                           'class': 'form-control',                 # class bootstrap
                           'placeholder': 'Input name of Train',     # надпись внутри поля
                           }))
    travel_time = forms.IntegerField(label='Travel time',
                                     widget=forms.NumberInput(attrs={
                                     'class': 'form-control',                 # class bootstrap
                                     'placeholder': 'Travel time',     # надпись внутри поля  
                                     }))
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={
                                         'class': 'form-control',
                                       }))
    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={
                                         'class': 'form-control',
                                       }))

    class Meta:
        model = Train
        fields = '__all__'