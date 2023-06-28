from rest_framework.customs import ComplexSerializer, PrimaryKeyRelatedField, SerializerMethodField
from .models import *


class Section_Serializer(ComplexSerializer):
    class Meta:
        model=Section
        fields="__all__"

