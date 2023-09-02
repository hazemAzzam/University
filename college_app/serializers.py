from university.customs import ComplexSerializer, StringRelatedField
from .models import *

class Department_Serializer(ComplexSerializer):
    minor_students = StringRelatedField(many=True, read_only=True)
    major_students = StringRelatedField(many=True, read_only=True)
    faculities = StringRelatedField(many=True, read_only=True)
    courses = StringRelatedField(many=True, read_only=True, required=False)
    class Meta:
        model=Department
        fields="__all__"

class College_Serializer(ComplexSerializer):
    departments = StringRelatedField(many=True, read_only=True)
    class Meta:
        model=College
        fields="__all__"