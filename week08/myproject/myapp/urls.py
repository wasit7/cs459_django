##restapi
from django.conf.urls import url
from rest_framework import routers
from myapp.views import CustomerViewSet, CarViewSet, RentViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'rents', RentViewSet)

urlpatterns = []
urlpatterns += 	router.urls