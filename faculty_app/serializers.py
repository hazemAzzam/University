from university.customs import ComplexSerializer, CharField, SerializerMethodField, SlugRelatedField, StringRelatedField, ModelSerializer
from .models import *
from person_app.serializers import Person_Serializer
from student_app.serializers import Student_Serializer


class Faculty_Serializer(Person_Serializer):
    chairs = StringRelatedField(read_only=True)
    class Meta:
        model=Faculty
        fields="__all__"

#class Instructor_Researcher_Serializer(ModelSerializer):
#    instructor = SerializerMethodField()
#    instructor_type = SlugRelatedField(slug_field="name", read_only=True)
#    class Meta:
#        model=Instructor_Researcher
#        fields="__all__"
#
#    def get_instructor(self, obj):
#
#        if obj.instructor_type.name == "faculty":
#            return Faculty.objects.get(ssn=obj.instructor_ssn).name
#        else:
#            return Grad_Student.objects.get(student__ssn=obj.instructor_ssn).student.name
        
class Instructor_Researcher_V2_Serializer(ModelSerializer):

    class Meta:
        model=Instructor_Researcher
        fields="__all__"

        
class Grant_Serializer(ModelSerializer):
    faculty_name = CharField(read_only=True, source="faculty.name")
    supports = StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Grant
        fields="__all__"

class Support_Serializer(ComplexSerializer):

    class Meta:
        model=Support
        fields="__all__"