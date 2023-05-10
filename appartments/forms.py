from django.forms import ModelForm
from .models import Appartment


class AppartmentForm(ModelForm):
    class Meta:
        model = Appartment
        fields = [
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'square_footage',
            'address',
        ]
