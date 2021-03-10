from django.db import models


class Parking(models.Model):

    name = models.CharField(max_length=80, default="")
    capacity = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.name, self.capacity)

    def _get_spots_tuple(self):
        spots = ParkingSpot.objects.filter(
            parking_id__id=self.id
        )
        res = [self]
        res.extend(list(spots))
        return res


class ParkingSpot(models.Model):

    parking_id = models.ForeignKey(
        Parking,
        on_delete=models.CASCADE,
        related_name="parking_spot",
    )
    name = models.CharField(max_length=80, default="")
