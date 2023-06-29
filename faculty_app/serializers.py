from rest_framework.customs import ComplexSerializer, CharField, SerializerMethodField, SlugRelatedField
from .models import *
from person_app.serializers import Person_Serializer
from student_app.serializers import Student_Serializer

class Faculty_Serializer(Person_Serializer):
    
    class Meta:
        model=Faculty
        fields="__all__"

class Instructor_Researcher_Serializer(ComplexSerializer):
    instructor = SerializerMethodField()
    instructor_type = SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model=Instructor_Researcher
        fields="__all__"

    def get_instructor(self, obj):
        if obj.instructor_type.name == "faculty":
            return Faculty.objects.get(ssn=obj.instructor_ssn).name
        else:
            print(Grade_Student.objects.get(student__ssn=obj.instructor_ssn))
            return Grade_Student.objects.get(student__ssn=obj.instructor_ssn).student.name