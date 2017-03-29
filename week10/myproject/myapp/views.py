##restapi
from rest_framework import viewsets
from myapp.models import Customer, CustomerSerializer
from myapp.models import Car, CarSerializer
from myapp.models import Rent, RentSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

#https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
from django.shortcuts import render
from django.views.generic import View
class Home(View):
	def get(self, request):
		return render(request, 'home.html', {'title': 'Home'})
	def post(self, request):
		return render(request, 'home.html', {'title': 'Home'})

