from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['image']


class HotelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Hotel
        fields = ['id','name','description','address','owner','photos']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'number', 'status', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields =['id', 'hotel', 'user', 'rating', 'comment']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'start_date', 'end_date', 'status']

