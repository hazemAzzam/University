from rest_framework.customs import ComplexSerializer, PrimaryKeyRelatedField, CharField, IntegerField, StringRelatedField, SlugRelatedField
from .models import *
from person_app.serializers import Person_Serializer
from datetime import datetime
from university.customs import get_current_quarter
from course_app.models import Section
from rest_framework.serializers import ValidationError
from django.db.models import Q
from faculty_app.models import Faculty

class Student_Serializer(Person_Serializer):
    class Meta:
        model=Student
        fields="__all__"


class Degree_Serializer(ComplexSerializer):
    class Meta:
        model=Degree
        fields='__all__'

class Degree_Serializer(ComplexSerializer):
    class Meta:
        model=Degree
        fields="__all__"

class Grade_Student_Serializer(ComplexSerializer):
    student_name = StringRelatedField(source="student")
    student = PrimaryKeyRelatedField(
        queryset=Student.objects.filter(
                Q(level=4, grade_student=None)
                |
                Q(level=5)
            ),
            write_only=True
    )
    grade = Degree_Serializer(required=True)
    level = IntegerField()
    advisor_name = StringRelatedField(source="advisor")
    advisor = PrimaryKeyRelatedField(queryset=Faculty.objects.all(), write_only=True)
    committee_names = StringRelatedField(source="committee", many=True, read_only=True)
    committee = PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        many=True,
        write_only=True
    )
    class Meta:
        model=Grade_Student
        fields=["student_name", "student", "level", "grade", "advisor_name", "advisor", "committee_names", "committee"]
    def create(self, validated_data):
        
        student = Student.objects.get(ssn=validated_data['student'].ssn)
        student_level = student.level
        new_level = validated_data.pop('level', 0)
        if new_level - student_level != 1:
            raise ValidationError("You can only level a student up 1 level")
        student.level = new_level
        student.save()


        return super().create(validated_data)
    

class Register_Serializer(ComplexSerializer):
    section = PrimaryKeyRelatedField(queryset=Section.objects.filter(year=datetime.now().year, qtr=get_current_quarter()))
    class Meta:
        model=Register
        fields="__all__"

class Transcript_Serializer(ComplexSerializer):
    section = PrimaryKeyRelatedField(queryset=Section.objects.filter(year=datetime.now().year, qtr=get_current_quarter()))
    class Meta:
        model=Transcript
        fields="__all__"
    