from rest_framework import serializers,validators
from .models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')
        extra_kwargs = {
            'password':{'write_only':True},
            'email':{
                'required':True,
                'validators':{
                    validators.UniqueValidator(
                        User.objects.all(),'A user with that email already exists'
                    )
                }
            }

        }
    def create(self,validated_data):
        username = validated_data('username')
        password = validated_data('password')
        email = validated_data('email')
        first_name = validated_data('first_name')
        last_name = validated_data('last_name')

        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        
        return user
        



class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = '__all__'

class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
