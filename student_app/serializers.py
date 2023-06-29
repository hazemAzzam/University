from rest_framework.customs import ComplexSerializer, PrimaryKeyRelatedField, CharField, IntegerField, StringRelatedField, FloatField
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

    def create(self, validated_data):
        if validated_data['level'] > 4:
            raise ValidationError("Please add student level 5 from grad student section")
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if validated_data['level'] > 4:
            raise ValidationError("Please add student level 5 from grad student section")
        return super().update(instance, validated_data)



class Grad_Student_Serializer(ComplexSerializer):
    student_name = StringRelatedField(source="student.name", read_only=True)
    student_level = IntegerField(source="student.level", read_only=True)
    advisor_name = StringRelatedField(source="advisor.name", read_only=True)
    committee_name = StringRelatedField(source='committee', many=True, read_only=True)

    student = PrimaryKeyRelatedField(
        queryset=Student.objects.filter(
                Q(level=4, grade_student=None)
                |
                Q(level=5)
            ),
        required=False
    )

    advisor = PrimaryKeyRelatedField(queryset=Faculty.objects.all(), write_only=True, required=False)
    committee = PrimaryKeyRelatedField(queryset=Faculty.objects.all(), write_only=True, many=True, required=False)

    collage = CharField(required=False)
    degree = FloatField(required=False)
    year = IntegerField(required=False)
    class Meta:
        model=Grad_Student
        fields="__all__"

    def create(self, validated_data): 
        grad_student = super().create(validated_data)
        grad_student.student.level = 5
        grad_student.student.save()
        return grad_student
    
    
    
#class Grade_Student_Serializer(ModelSerializer):
#    student_name = StringRelatedField(source="student")
#    student = PrimaryKeyRelatedField(
#        queryset=Student.objects.filter(
#                Q(level=4, grade_student=None)
#                |
#                Q(level=5)
#            ),
#            write_only=True
#    )
#    grade = Degree_Serializer(required=True)
#    level = IntegerField(source="student.level")
#    advisor_name = StringRelatedField(source="advisor")
#    advisor = PrimaryKeyRelatedField(queryset=Faculty.objects.all(), write_only=True)
#    committee_names = StringRelatedField(source="committee", many=True, read_only=True)
#    committee = PrimaryKeyRelatedField(
#        queryset=Faculty.objects.all(),
#        many=True,
#        write_only=True
#    )
#    class Meta:
#        model=Grad_Student
#        fields=["student_name", "student", "level", "grade", "advisor_name", "advisor", "committee_names", "committee"]
#        
#    def create(self, validated_data):
#        grad_student= super().create(validated_data)
#
#        #student = Student_Serializer(instance=grad_student.student)
#        #student.update(level=validated_data['level'])
#
#        return grad_student


        
    

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
    