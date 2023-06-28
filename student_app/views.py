from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Student_View(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Student_Serializer

class Grade_Student_View(ModelViewSet):
    queryset=Grade_Student.objects.all()
    serializer_class=Grade_Student_Serializer

class Register_View(ModelViewSet):
    queryset=Register.objects.all()
    serializer_class=Register_Serializer

class Transcript_View(ModelViewSet):
    queryset=Transcript.objects.all()
    serializer_class=Transcript_Serializer