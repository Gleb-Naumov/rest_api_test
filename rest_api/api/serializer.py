from rest_framework import serializers

from .models import EducationalModules


class EducationalSerialiser(serializers.Serializer):
    class Meta:
        model = EducationalModules
        fields = ('id', 'name', 'description')
