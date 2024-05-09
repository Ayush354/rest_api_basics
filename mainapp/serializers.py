from rest_framework import serializers
from  mainapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','score']

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields = ['id','first_name','last_name','travelpoints']

        