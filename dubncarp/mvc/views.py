from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Admin_class,Customer_class,Seller_class
from .models import Customer,Seller,Admin_model
from .forms import My_form
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def suman():
    return HttpResponse('DONE')

class Admin(APIView):

    def get(self,request):
        querysets=Admin_model.objects.all()
        serializers=Admin_class(data=querysets,many=True)
        print(querysets)
        print(serializers)
        if Admin_model.DoesNotExist:
            return Response({'error':"Admin not found"})
        return Response(serializers.data)
    

    def post(self,request):
        # serializers=Admin_class(data=request)
        serializer = Admin_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            request.data.get('email')
            customer_id= request.data.get('customer_id')
            customer_name=request.data.get('customer_name')
            customer_email=request.data.get('customer_email')
            customer_contact = request.data.get('customer_contact')


            seller_id=request.data.get('seller_id')
            seller_name=request.data.get('seller_name')
            seller_email=request.data.get('seller_email')
            seller_contact=request.data.get('seller_contact')

            # customer_id=21
            # customer_name='suman'
            # customer_email='suman@gakil.com'
            # customer_contact = '973283888'


            Customer_datas={
                "Customer_id": customer_id,
                "Customer_name": customer_name,
                "email":customer_email,
                "phone": customer_contact
                }
            
            Seller_datas={
                "Seller_id":seller_id,
                "Seller_name":seller_name,
                "email":seller_email,
                "phone":seller_contact
            }

            serializer.save()
            serializer_customer=Customer_class(data=Customer_datas)
            if serializer_customer.is_valid():
                serializer_customer.save()
                print('***CUSTOMER CREATED***')
            serializer_seller=Seller_class(data=Seller_datas)
            if serializer_seller.is_valid():
                serializer_seller.save()
                print('***sELLER CREATED***')

            return Response('DOne')
        return Response('wrong')



class delete_customer(APIView):
    def delete(self,request,item_id):
        try:
            customer=Customer.objects.get( Customer_id=item_id)
            
        except Customer.DoesNotExist:
            return Response ({"error":"Customer not found"},status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response ('Customer has delete sucessfully')


class delete_seller(APIView):
    def delete(self,request,item_id):
        try:
            customer=Seller.objects.get(Seller_id=item_id)
            
        except Customer.DoesNotExist:
            return Response ({"error":"Seller not found"},status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response ('Seller has delete sucessfully')


class customer(APIView):
    def post(self,request):

        return Response('Done')


# class form_post(APIView):
#     def post(request):
#         form=My_form(data=request.data)
#         if form.is_valid():
#             form.save()
#             return Response("MY_FORM IS SAVED !")
#         return Response('******
#')
def set(request):
    context={}
    form =My_form(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        context['form']=form
        return render(request,'home.html',context)
    

def loading(request):
    
    
    mydata=Admin_model.objects.all()
    print(mydata)
    
    template=loader.get_template('dell/one.html')
    
    context={
        'mycustomer':mydata,
    }
    return HttpResponse(template.render(context,request))


# def rendertemp():
    
#     return render ('f.html')

