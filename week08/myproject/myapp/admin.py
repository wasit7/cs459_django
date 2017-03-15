from django.contrib import admin
from myapp.models import Customer, Car, Rent

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]
admin.site.register(Customer,CustomerAdmin)

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
	list_editable=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
admin.site.register(Rent,RentAdmin)