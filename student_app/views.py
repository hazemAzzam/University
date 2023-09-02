from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from faculty_app.models import Instructor_Researcher
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to specify page size using ?page_size=
    max_page_size = 100  # Maximum page size to prevent abuse


class Student_View(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Student_Serializer
    pagination_class = CustomPagination

class Grad_Student_View(ModelViewSet):
    queryset=Grad_Student.objects.all()
    serializer_class=Grad_Student_Serializer

    def retrieve(self, request, *args, **kwargs):
        student = kwargs['pk']
        print(student)
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def increase_level(self, request, pk=None):
        try:
            grad_student = Grad_Student.objects.get(student=pk)
            grad_student.student.level += 1
            if grad_student.student.level > 6:
                raise ValidationError("Cannot increase student level more than 6")
            grad_student.student.save()
            return Response(Grad_Student_Serializer(instance=grad_student).data)
        except:
            raise ValidationError("cannot increase student level")
        
    @action(detail=True, methods=['post'])
    def decrease_level(self, request, pk=None):
        try:
            grad_student = Grad_Student.objects.get(student=pk)
            grad_student.student.level -= 1
            if grad_student.student.level <= 4:
                student = Student_Serializer(instance=grad_student.student).data
                self.destroy(request, pk)
                grad_student.delete()
                return Response(student)
            grad_student.student.save()
            return Response(Grad_Student_Serializer(instance=grad_student).data)
        except:
            raise ValidationError("cannot decrease student level")
        
    def destroy(self, request, pk, *args, **kwargs):
        student_ssn = pk
        Instructor_Researcher.objects.get(instructor_ssn=student_ssn).delete()
        return super().destroy(request, *args, **kwargs)
        
        



class Register_View(ModelViewSet):
    queryset=Register.objects.all()
    serializer_class=Register_Serializer

class Transcript_View(ModelViewSet):
    queryset=Transcript.objects.all()
    serializer_class=Transcript_Serializer