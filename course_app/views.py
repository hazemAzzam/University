from rest_framework.viewsets import ModelViewSet
from .serializers import *
from datetime import datetime
from university.customs import get_current_quarter

    
class Section_View(ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=Section_Serializer

class Current_Section_View(ModelViewSet):
    queryset=Section.objects.filter(year=datetime.now().year, qtr=get_current_quarter())
    serializer_class=Section_Serializer