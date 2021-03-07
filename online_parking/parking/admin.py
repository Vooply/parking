from django.contrib import admin
from parking.models import Parking, ParkingSpot


class parkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


admin.site.register(Parking, parkingAdmin)
admin.site.register(ParkingSpot)
