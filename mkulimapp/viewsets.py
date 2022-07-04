from rest_framework import viewsets
from . import models
from . import serializers


class FarmerViewset(viewsets.ModelViewSet):
    queryset = models.Farmer.objects.all()
    serializer_class = serializers.FarmerSerializer

class VendorViewset(viewsets.ModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

class MerchandiseViewset(viewsets.ModelViewSet):
    queryset = models.Merchandise.objects.all()
    serializer_class = serializers.MerchandiseSerializer

class FeedsViewset(viewsets.ModelViewSet):
    queryset = models.Feeds.objects.all()
    serializer_class = serializers.FeedsSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer



