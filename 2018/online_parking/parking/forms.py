from django import forms

from parking.models import Parking


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('name', 'capacity')

        def clean(self):
            pass
