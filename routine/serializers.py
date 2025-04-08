from rest_framework import serializers
from .models import RoutineModels

class RoutineSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoutineModels
    fields = '__all__'
