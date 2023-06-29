from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework.response import Response

class Student_View(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Student_Serializer

class Grad_Student_View(ModelViewSet):
    queryset=Grad_Student.objects.all()
    serializer_class=Grad_Student_Serializer

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
                grad_student.delete()
                return Response(student)
            grad_student.student.save()
            return Response(Grad_Student_Serializer(instance=grad_student).data)
        except:
            raise ValidationError("cannot decrease student level")
        
        



class Register_View(ModelViewSet):
    queryset=Register.objects.all()
    serializer_class=Register_Serializer

class Transcript_View(ModelViewSet):
    queryset=Transcript.objects.all()
    serializer_class=Transcript_Serializer