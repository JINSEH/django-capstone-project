from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializer import UserSerializer, MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [permissions.IsAuthenticated]


@api_view()
@permission_classes([permissions.IsAuthenticated])
def msg(request):
  return JsonResponse({'message' : 'This view is protected'})