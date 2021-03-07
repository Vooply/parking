from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse

from parking.models import Parking
from parking.forms import ParkingForm


# Create your views here.
class TestView(View):

    def get(self, request):
        return HttpResponse("Hello world!")


class ParkingView(View):

    def get(self, request):
        result = {}
        for parking in Parking.objects.all():
            result[parking.id] = parking._get_spots_tuple()
        return render(request, 'test.html', context={'data': result.items()})


class AddParking(View):

    def get(self, request):
        form = ParkingForm()
        return render(request, "add_parking.html", {'form': form})

    def post(sels, request):
        form = ParkingForm(request.POST)
        if form.is_valid():
            new_parking = Parking(
                name=form.cleaned_data["name"],
                capacity=form.cleaned_data["capacity"],
            )
            new_parking.save()
            return HttpResponseRedirect(reverse('parkings'))
        else:
            return render(request, "add_parking.html", {'form': form})
