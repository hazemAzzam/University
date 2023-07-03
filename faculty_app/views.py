from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .filters import *

class Faculty_View(ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=Faculty_Serializer

    def destroy(self, request, *args, **kwargs):
        faculty_ssn = kwargs['pk']
        Instructor_Researcher.objects.get(instructor_ssn=faculty_ssn).delete()
        return super().destroy(request, *args, **kwargs)

#class Instructor_Researcher_View(ModelViewSet):
#    queryset=Instructor_Researcher.objects.all()
#    serializer_class=Instructor_Researcher_Serializer

class Instructor_Researcher_V2_View(ModelViewSet):
    queryset=Instructor_Researcher.objects.all()
    serializer_class=Instructor_Researcher_V2_Serializer

class Grant_View(ModelViewSet):
    queryset=Grant.objects.all()
    serializer_class=Grant_Serializer

class Support_View(ModelViewSet):
    queryset=Support.objects.all()
    serializer_class=Support_Serializer
    filterset_class=Support_Filters