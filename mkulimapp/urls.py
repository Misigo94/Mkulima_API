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




urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login_api),
    path('user/',views.get_user_data),
    path('register/',views.register_api),
    path('api/farmer',views.FarmerList.as_view()),
    path('api/farmer/details/<str:pk>',views.FarmerDetail.as_view()),
    path('api/vendor',views.VendorList.as_view()),
    path('api/vendor/details/<str:pk>',views.VendorDetail.as_view()),
    path('api/feeds',views.FeedsList.as_view()),
    path('api/feeds/details/<str:pk>',views.FeedsDetail.as_view()),
    path('api/merchandise',views.MerchandiseList.as_view()),
    path('api/merchandise/details/<str:pk>',views.MerchandiseDetail.as_view()),
    path('api/category',views.CategoryList.as_view()),
    path('api/category/details/<str:pk>',views.CategoryDetail.as_view()),
    path('api/comment',views.CommentList.as_view()),
    path('api/comment/details/<str:pk>',views.CommentDetail.as_view()),
    path('feeds/',views.feedsdata,name='feed'),

]
