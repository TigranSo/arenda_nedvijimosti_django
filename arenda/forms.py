from django import forms
from .models import Reservation, Applications, Region, Arenda
from django.utils.translation import gettext_lazy as _


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['arrival', 'departure', 'full_name', 'phone', 'email', 'preferences']
        widgets = {
            'arrival': forms.DateInput(attrs={'type': 'date'}),
            'departure': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'arrival': _('Arrival'),
            'departure': _('Departure'),
            'full_name': _('Full Name'),
            'phone': _('Phone'),
            'email': _('Email'),
            'preferences': _('Preferences'),
        }

class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'email', 'tel']
        
        
class SearchForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=True,
        label='Регион',
        widget=forms.Select(attrs={'class': 'form-control custom-class'}),
        initial=None, 
        empty_label="Регион"  
    )
    
    property_type_2 = forms.ChoiceField(
        choices=Arenda.PROPERTY_CHOICES_2,
        required=True,
        label='Аренда или Купить?',
        widget=forms.Select(attrs={'class': 'form-control custom-class'})
    )
    
    property_type = forms.ChoiceField(
        choices=[('', 'Тип жилья')] + Arenda.PROPERTY_CHOICES,
        required=True,
        label='Тип жилья',
        widget=forms.Select(attrs={'class': 'form-control custom-class'}),
        initial='',
    )
    
    rooms = forms.CharField(
        required=False,
        label=_('Number of Rooms'),  
        widget=forms.TextInput(attrs={'class': 'form-control custom-class custom-class_1', 'placeholder': _('Number of Rooms')})
    )

    price_min = forms.DecimalField(
        required=False,
        label=_('Price Minimum'), 
        widget=forms.NumberInput(attrs={'class': 'form-control custom-class custom-class_1', 'placeholder': _('Price Minimum')})
    )

    price_max = forms.DecimalField(
        required=False,
        label='',
        widget=forms.NumberInput(attrs={'class': 'form-control custom-class custom-class_1', 'placeholder': 'Цена до'})
    )
        
        