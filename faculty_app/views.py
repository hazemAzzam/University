from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .filters import *

class Faculty_View(ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=Faculty_Serializer

class Instructor_Researcher_View(ModelViewSet):
    queryset=Instructor_Researcher.objects.all()
    serializer_class=Instructor_Researcher_Serializer

class Grant_View(ModelViewSet):
    queryset=Grant.objects.all()
    serializer_class=Grant_Serializer

class Support_View(ModelViewSet):
    queryset=Support.objects.all()
    serializer_class=Support_Serializer
    filterset_class=Support_Filters