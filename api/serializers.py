from django.contrib.auth.models import User
from rest_framework import serializers
from restaurant.models import Booking, MenuItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']