# Setup
## myproject/myapp/models.py
```python
from rest_framework import serializers
# models
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('name','dob')
```

## myproject/myapp/urls.py
```python
from django.conf.urls import url
from rest_framework import routers
from myapp.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
urlpatterns = []
urlpatterns += 	router.urls
```

## myproject/myapp/views.py
```python
from rest_framework import viewsets
from myapp.models import Customer, CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
```

## myproject/settings.py
```python
INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'myapp',
     'rest_framework'
 ]

```

## myproject/urls.py
```python
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^myapp/', include('myapp.urls', namespace="myapp") ),
]

```

# Methods

method | with id | description
-------|---------|-----------
GET | no |listing all records
GET | yes | get the item
POST | no | creating an item
PUT | yes | update the item
PATCH | yes | update the item
DELETE | yes | delete the item

# End-points

``` batch
GET		http://localhost:8000/myapp/cars/
GET 	http://localhost:8000/myapp/cars/[car_id]
POST 	http://localhost:8000/myapp/cars/
PUT		http://localhost:8000/myapp/cars/[car_id]
PATCH	http://localhost:8000/myapp/cars/[car_id]
DELETE	http://localhost:8000/myapp/cars/[car_id] 


GET		http://localhost:8000/myapp/customers/
GET 	http://localhost:8000/myapp/customers/[customer_id]
POST 	http://localhost:8000/myapp/customers/
PUT		http://localhost:8000/myapp/customers/[customer_id]
PATCH	http://localhost:8000/myapp/customers/[customer_id]
DELETE	http://localhost:8000/myapp/customers/[customer_id]


GET		http://localhost:8000/myapp/rents/
GET 	http://localhost:8000/myapp/rents/[rent_id]
POST 	http://localhost:8000/myapp/rents/
PUT		http://localhost:8000/myapp/rents/[rent_id]
PATCH	http://localhost:8000/myapp/rents/[rent_id]
DELETE	http://localhost:8000/myapp/rents/[rent_id]
```
