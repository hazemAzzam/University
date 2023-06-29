from rest_framework.customs import ComplexSerializer, PrimaryKeyRelatedField, SerializerMethodField, ModelSerializer
from .models import *


class Section_Serializer(ComplexSerializer):
    class Meta:
        model=Section
        fields="__all__"

class Course_Serializer(ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
