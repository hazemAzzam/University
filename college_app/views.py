from rest_framework.viewsets import ModelViewSet
from .serializers import *

class College_View(ModelViewSet):
    queryset=College.objects.all()
    serializer_class=College_Serializer

class Department_View(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=Department_Serializer