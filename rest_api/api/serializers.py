from rest_framework import serializers

from .models import EducationalModules


class EducationalSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationalModules
        fields = ('id', 'name', 'description')
