from django.test import TestCase
from .models import Department

class DepartmentModelTest(TestCase):

    def test_department_creation(self):
        department = Department.objects.create(name="IT", description="Information Technology")
        self.assertEqual(department.name, "IT")