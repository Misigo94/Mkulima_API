from calendar import c
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
import requests


# Create your views here.

def index(request):
    try:
        feed = Feeds.objects.all()
    
        return render(request, 'index.html', {'feed':feed})

    except feed.DoesNotExist:
        return HttpResponse('no feed found')


def getfeed(request,id):

    feed= Feeds.objects.get(id=id)



    return render(request, 'found.html',{'feed':feed})        


class FarmerList(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class =FarmerSerializer

class FarmerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class =VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class FeedsList(generics.ListCreateAPIView):
    queryset = Feeds.objects.all()
    serializer_class =FeedsSerializer

class FeedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer

class MerchandiseList(generics.ListCreateAPIView):
    queryset = Merchandise.objects.all()
    serializer_class =MerchandiseSerializer

class MerchandiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




def feedsdata(request):

    response_json = requests.get('http://127.0.0.1:8000/api/feeds/') 
    if (response_json.status_code == 200):  
        response = response_json.json()
        print(response)

    context = {
        'feeds': response
    }     



    return render(request , 'feed.html',context)    






    
