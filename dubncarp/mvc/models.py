from django.db import models


class Admin_model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_id=models.IntegerField(null=True,default=0)
    customer_name= models.CharField(max_length=50,null=True)
    customer_email= models.CharField(max_length=50,unique=True,null=True)
    customer_contact = models.CharField(max_length=15, blank=True, null=True)
    seller_id=models.IntegerField(null=True,default=0)
    seller_name= models.CharField(max_length=50,null=True)
    seller_email= models.CharField(max_length=50,unique=True,null=True)
    seller_contact = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.username
    
class Customer(models.Model):
    Customer_id=models.IntegerField(blank=True)
    Customer_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Customer_name

class Seller(models.Model):
    Seller_id=models.IntegerField(blank=True)
    Seller_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Seller_name







# {
#   "first_name": "John",
#   "last_name": "Doe",
#   "username": "johndoe",
#   "email": "johndoe@example.com",
#   "created_at": "2025-03-21T12:00:00Z",
#   "updated_at": "2025-03-21T12:30:00Z",
#   "customer_id": 12345,
#   "customer_name": "John Doe",
#   "customer_email": "customer@example.com",
#   "customer_contact": "+1234567890",
#   'seller_id':78,
#   'seller_name':'swudj',
#   'seller_email':'hsudmn@hi.com',
#   'seller_contact':'+19929383838484'
# }



# {
#   "first_name": "Johnzz",
#   "last_name": "Doezz",
#   "username": "johndozze123",
#   "email": "johndoe@exazzmple.com",
#   "created_at": "2025-03-24T10:15:30Z",
#   "updated_at": "2025-03-24T12:45:00Z",
#   "customer_id": 10,
#   "customer_name": "zzJohn's Store",
#   "customer_email": "cuzzstomer@example.com",
#   "customer_contact": "+12234567890",
#   "seller_id": 2,
#   "seller_name": "zzDoe Supplies",
#   "seller_email": "sezzller@example.com",
#   "seller_contact": "+1987654321"
# }
