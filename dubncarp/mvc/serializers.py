from rest_framework import serializers
from .models import Admin_model,Customer,Seller

class Admin_class(serializers.ModelSerializer):
    class Meta:
        model=Admin_model
        fields='__all__'

class Customer_class(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class Seller_class(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields='__all__'