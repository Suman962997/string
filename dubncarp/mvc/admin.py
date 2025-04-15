from django.contrib import admin
from .models import Customer,Seller,Admin_model

admin.site.register(Admin_model)
admin.site.register(Customer)
admin.site.register(Seller)


