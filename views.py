from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=['get'])
    def employee_count(self, request, pk=None):
        department = self.get_object()
        employee_count = department.employee_set.count()
        return Response({'employee_count': employee_count})