from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'flight_type', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return price