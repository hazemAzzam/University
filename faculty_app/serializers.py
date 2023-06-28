from rest_framework.customs import ComplexSerializer, CharField
from .models import *
from person_app.serializers import Person_Serializer

class Faculty_Serializer(Person_Serializer):
    
    class Meta:
        model=Faculty
        fields="__all__"

class Instructor_Researcher_Serializer(ComplexSerializer):
    
    class Meta:
        model=Instructor_Researcher
        fields="__all__"