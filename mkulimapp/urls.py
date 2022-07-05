from django.urls import path
from mkulimapp import views
from .models import *
from knox import views as knox_views


urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login_api),
    path('user/',views.get_user_data),
    path('register/',views.register_api),
    path('logout/',knox_views.LogoutView.as_view()),
    path('logoutall/',knox_views.LogoutAllView.as_view()),
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

    path('found/<str:id>/',views.getfeed,name='found'),
]