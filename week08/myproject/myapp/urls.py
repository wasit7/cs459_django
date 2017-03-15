from django.conf.urls import url
from rest_framework import routers
from myapp.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
urlpatterns = []
urlpatterns += 	router.urls