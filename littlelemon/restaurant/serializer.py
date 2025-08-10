from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only = True,
    required=True,
    style={'input_type': 'password'}
  )

  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups', 'password']

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']
    )
    return user

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields = '__all__'