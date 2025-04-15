from django.shortcuts import render
from .models import Gateway
from .serializers import Gateway_class
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .forms import PostForm
from rest_framework import viewsets



class General_api(APIView):
    def post(self,request):
        data=request.data
        Companys=data['Company']+'EDIT'
        Blocks=data['Block']
        Floars=data['Floar']
        Rents=data['Rent']
        
        datas={
            "Company":Companys,
            "Block":Blocks,
            "Floar":Floars,
            "Rent":Rents
        }
        serializer=Gateway_class(data=datas)
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
class view_api(APIView):
    def get(self,request):
        queryset=Gateway.objects.all()
        serializer=Gateway_class(queryset,many=True)
        return Response(serializer.data)
    
class get_one(APIView):
    def get(self,request,pk):
        try:
            post=Gateway.objects.get(id=pk)
            serializer=Gateway_class(post)
            return Response(serializer.data)
        except post.DoesNotExist:
            return Response({"Error":"Post not found"},status=status.HTTP_200_OK)


class viewport(generics.ListAPIView):
    queryset=Gateway.objects.all()
    serializer_class=Gateway_class


class forforms(generics.CreateAPIView):
    queryset=Gateway.objects.all()
    serializer_class=Gateway_class
    def create(self,request,*args,**kwargs):
        form=PostForm(request.data)
        if form.is_valid():
            post=form.save()
            serializer=self.get_serializer(post)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response('NOT SAVED',status=status.HTTP_502_BAD_GATEWAY)

class view_forms(generics.ListAPIView):
    queryset=Gateway.objects.all()
    serializer_class=Gateway_class
    def view(self,request,*args,**kwargs):
        datas=Gateway.objects.all()
        print(datas)
        return datas

# class post_and_get(generics.ListCreateAPIView):
    
    
# *************************************************************************






class postviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Gateway.objects.all()
        serializer=Gateway_class(queryset,many=True)
        return Response(serializer.data)


    def create(self,request):
        serializer=Gateway_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('SAVED',status=status.HTTP_100_CONTINUE)
        return Response('NOT SAVE',status=status.HTTP_502_BAD_GATEWAY)
    
    
    def retrive(self,request,pk=None):
        try:
            model=Gateway.objects.get(pk=pk)
        except Gateway.DoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer=Gateway_class(model)
        
        return Response(serializer.data,status.HTTP_100_CONTINUE)






















