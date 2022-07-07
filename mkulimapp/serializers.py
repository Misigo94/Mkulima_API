from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers, validators


class UserSerializer(serializers.ModelSerializer):
    	class Meta:
            model = User
            fields = ['id', 'name', 'email', 'password']
            extra_kwargs = {
                'password': {'write_only': True}
            }
        
	
        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance



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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that email already exists"
                    )
                ]
            }
        }


def create(self, validated_data):
    username = validated_data.get('username')
    password = validated_data.get('password')
    email = validated_data.get('email')
    first_name = validated_data.get('first_name')
    last_name = validated_data.get('last_name')

    user = User.objects.create(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )

    return user
