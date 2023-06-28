from django.db import models
from person_app.models import Person

class Faculty(Person):
    rank = models.IntegerField()
    f_office = models.IntegerField()
    f_phone = models.CharField(max_length=15)
    salary = models.PositiveIntegerField()
    
    
class Instructor_Researcher(models.Model):
    grade_student = models.OneToOneField("student_app.Grade_Student", on_delete=models.SET_NULL, null=True, related_name="instructor_researcher")
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, related_name="instructor_of")

