from django.test import TestCase
from restaurant.models import Booking, MenuItem
from django.utils import timezone


class BookingTest(TestCase):
    def test_get_booking(self):
        current_datetime = timezone.now()
        booking = Booking.objects.create(name="John Doe", no_of_guests=11, booking_date=current_datetime)
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 11)
        self.assertEqual(booking.booking_date, current_datetime)

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Chocolate", price=15, inventory=50)
        self.assertEqual(item.title, "Chocolate")
        self.assertEqual(item.price, 15)
        self.assertEqual(item.inventory, 50)

