from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=100, null=True, blank=True)
	dob=models.DateField(null=True, blank=True)
class Car(models.Model):
	model_name=models.CharField(max_length=100, null=True, blank=True)
	price=models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	milage=models.FloatField(blank=True, null=True)
class Rent(models.Model):
	customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
	car=models.ForeignKey(Car,  on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name','dob')