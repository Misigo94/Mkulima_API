from django.urls import path
from mkulimapp import views
from .models import *
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),

]
