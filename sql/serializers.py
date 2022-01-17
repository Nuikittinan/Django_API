from rest_framework import serializers
from .models import Todolist
from django.contrib.auth.models import User
from .models import *
from django.db.models import fields

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id','title','detail','birthday','age','gender','date') #'__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'is_superuser', 'username', 'first_name', 'last_name']
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAll
        fields = ['temp', 'spo2', 'hr','create']

# class Spo2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeviceAll
#         fields = ['spo2', 'create']

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAll
        fields = ['hr']

# class Spo2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeviceAll
#         fields = ['spo2']
        
# class HRSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeviceAll
#         fields = ['hr', 'create']
# ควยยย