##restapi
from django.conf.urls import url
from rest_framework import routers
from myapp.views import CustomerViewSet, CarViewSet, RentViewSet
from myapp.views import Home
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'rents', RentViewSet)

urlpatterns = [
	url(r'^home/$', Home.as_view()),
]
urlpatterns += 	router.urls