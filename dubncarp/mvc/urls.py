from django.urls import path
from .views import suman,Admin,delete_customer,delete_seller,set,loading
urlpatterns=[
    # path('create_folder/',create_folder,name='create_folder')
    path('suman/',suman,name='suman'),
    path('adm/',Admin.as_view(),name='Admin'),
    path('delete_customer/<int:item_id>/',delete_customer.as_view(),name='Delete_customer'),
    path('delete_seller/<int:item_id>',delete_seller.as_view(),name='Delete_seller'),
    path('new',set,name='My_new_form'),
    path('loader/',loading,name='loader'),
    # path('ren/',rendertemp,name='temp')
]