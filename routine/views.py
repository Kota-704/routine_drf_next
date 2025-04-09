from rest_framework import viewsets
from .models import RoutineModels
from .serializers import RoutineSerializer

class RoutineViewSet(viewsets.ModelViewSet):
  queryset = RoutineModels.objects.all()
  serializer_class = RoutineSerializer
