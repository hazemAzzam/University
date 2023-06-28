from rest_framework.serializers import ModelSerializer, CharField
from .models import *
from rest_framework.customs import ComplexSerializer

class Name_Serializer(ComplexSerializer):
    class Meta:
        model = Name
        fields=['fname', 'minit', 'lname']

class Address_Serializer(ComplexSerializer):
    class Meta:
        model=Address
        fields="__all__"

class Person_Serializer(ComplexSerializer):
    name = Name_Serializer(required=True)
    address = Address_Serializer(required=False)
    full_name = CharField(read_only=True)
    class Meta:
        model = Person
        fields = ['ssn', 'name','full_name', 'birth_date', 'sex', 'address']

