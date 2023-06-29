import django_filters
from .models import Support

class Support_Filters(django_filters.FilterSet):
    class Meta:
        model=Support
        fields=['grant']