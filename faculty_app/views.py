from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Faculty_View(ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=Faculty_Serializer

class Instructor_Researcher_View(ModelViewSet):
    queryset=Instructor_Researcher.objects.all()
    serializer_class=Instructor_Researcher_Serializer