from .models import EducationalModules
from .serializer import EducationalSerialiser
from rest_framework import viewsets


class EducationalViewSet(viewsets.ModelViewSet):
    queryset = EducationalModules.objects.all()
    serializer_class = EducationalSerialiser
