##restapi
from rest_framework import viewsets
from myapp.models import Customer, CustomerSerializer
from myapp.models import Car, CarSerializer, CarFilterSerializer
from myapp.models import Rent, RentSerializer
from django.db.models import Max
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CarViewSet(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer
	@list_route(methods=['POST'])
	def filter(self, request):
		filter = CarFilterSerializer(data=request.data)
		filter.is_valid(raise_exception=True)
		print(filter.validated_data)
		cars = self.get_queryset().filter(price__gte=filter.validated_data.get('min_price', 0), milage__gte=filter.validated_data.get('min_milage', 0))
		if filter.validated_data.get('max_price'):
			cars = cars.filter(price__lte=filter.validated_data.get('max_price'))
		if filter.validated_data.get('max_milage'):
			cars = cars.filter(milage__lte=filter.validated_data.get('max_milage'))
		print(len(cars))
		return Response(self.get_serializer(cars, many=True).data)

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

#https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
from django.shortcuts import render
from django.views.generic import View
class Home(View):
	def get(self, request):
		return render(request, 'home.html', {
			'title': 'Home', 
			'max_price': Car.objects.all().aggregate(Max('price'))['price__max'],
			'max_milage': Car.objects.all().aggregate(Max('milage'))['milage__max'],
			})
	def post(self, request):
		return render(request, 'home.html', {'title': 'Home'})

