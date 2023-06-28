from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Person_View(ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=Person_Serializer