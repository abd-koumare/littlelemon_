from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} : {str(self.booking_date)}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'