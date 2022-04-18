from django.contrib.auth.models import User
from djangorestapp.serializer import UserSerializer
from django.shortcuts import render,get_object_or_404,redirect
from djangorestapp.models import Article
from django.template import response
from rest_framework import serializers
from djangorestapp.serializer import ArticleSerializer
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse, request
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from djangorestapp import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform

class ArticleList(APIView):
    def get(self,request):
       arti=Article.objects.all()
       serializer = ArticleSerializer(arti, many=True)
       return Response(serializer.data)    
    def post(self,request):
            
            serializer=ArticleSerializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data,status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_200_OK)

class ArticleDetails(APIView):
            def get_objects(self,id):
                   
                        return Article.objects.get(id)
                     
            def get(self,request,id):
                arti=self.get_objects(id)
                serializer= ArticleSerializer(arti)
                return Response(serializer.data) 

            def put(self,request,id):
                serializer=ArticleSerializer(data=request.data)
                if serializer.is_valid:
                    
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)

                return Response(serializer.data,status=status.HTTP_200_OK)
            def delete(self,request,id):
                arti=self.get_objects(id)
                arti.delete()
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class registerUser(APIView):
    def some(request):
         
        from1=forms.createuserform()
        print(from1)

        return render(request,'index.html',{'userform': from1})
        
        
    def get(self,requset):
        print("gese")
        return render(request, "index.html")
    def post(self,request): 
       
            serializer=UserSerializer(data=request.data,partial=True)
            if not serializer.is_valid():
                print()
            
            serializer.save()
            print(serializer.data)
            user= User.objects.get(username=serializer.data['username'])
            token_obj ,_ =Token.objects.get_or_create(user=user)
            

            
            print(serializer.data)
            return Response({'status':200,'payload': serializer.data,'token':str(token_obj)})
          
             
        

"""
# Create your views here.
@api_view(['GET','POST'])
def articlelist(request):
    if request.method == "GET":
       
        arti=Article.objects.all()
        serializer = ArticleSerializer(arti, many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer=ArticleSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
 
        return Response(serializer.errors, status=status.HTTP_200_OK)
    
 
@api_view(['GET','PUT','DELETE'])
def articledetails(request,pk):
        
            
             
   
        arti =Article.objects.get(pk=pk)
     
        if request.method=="GET":
            serializer= ArticleSerializer(arti)
            return Response(serializer.data)   
        if request.method =="PUT":        
             data = JSONParser().parse(request)
             serializer=ArticleSerializer(arti,data=data)
             if serializer.is_valid():
                serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
        if request.method == "DELETE":
            arti.delete()
            return Response(status=status.HTTP_200_OK)
        
         
"""