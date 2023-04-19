from rest_framework import viewsets

from .models import EducationalModules
from .serializers import EducationalSerializers


class EducationalViewSet(viewsets.ModelViewSet):
    queryset = EducationalModules.objects.all()
    serializer_class = EducationalSerializers
