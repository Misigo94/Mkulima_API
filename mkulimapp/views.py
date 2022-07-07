from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import jwt, datetime


# Create your views here.

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        'token':token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        })
    return Response({'error':'not authenticated'}, status=400)

@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)


    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        'token':token
    })

def index(request):
    try:
        feed = Merchandise.objects.all()

        return render(request, 'index.html', {'feed': feed})

    except feed.DoesNotExist:
        return HttpResponse('no feed found')

# LOGIN VIEW


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
        })

    return Response({'error': 'not authenticated'}, status=400)


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token
    })


def getfeed(request, id):
    feed = Feeds.objects.get(id=id)
    return render(request, 'found.html', {'feed': feed})


class FeedsList(generics.ListCreateAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer


class FeedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer


class MerchandiseList(generics.ListCreateAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer


class MerchandiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


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

    return render(request, 'feed.html', context)


# Added These code below
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user  = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')
        
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            "jwt": token
        }
        
        return response


class UserView(APIView):
    
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Log out Success"
        }
        return response
