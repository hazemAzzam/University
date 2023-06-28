from rest_framework.serializers import ModelSerializer, CharField
from .models import *
from rest_framework.customs import ComplexSerializer

class Address_Serializer(ComplexSerializer):
    class Meta:
        model=Address
        fields="__all__"

class Person_Serializer(ComplexSerializer):
    name = CharField(read_only=True)
    address = Address_Serializer(required=False)

    class Meta:
        model = Person
        fields = ['ssn', 'name', 'fname', 'minit', 'lname', 'birth_date', 'sex', 'address']

