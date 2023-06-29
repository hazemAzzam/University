from django.db import models
from person_app.models import Person
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

class Student(Person):
    level = models.IntegerField()
    
class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='current_sections')
    section = models.ForeignKey("course_app.Section", on_delete=models.SET_NULL, null=True)

class Grad_Student(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grade_student", unique=True, primary_key=True)
    
    collage = models.CharField(max_length=50)
    degree = models.FloatField()
    year = models.IntegerField()

    @property
    def level(self):
        return f"{self.student.level}"
    advisor = models.ForeignKey("faculty_app.Faculty", related_name="advisor_of", on_delete=models.SET_NULL, null=True)
    committee = models.ManyToManyField("faculty_app.Faculty", related_name="committee")

    def __str__(self):
        return f"{self.student}"

    



class Transcript(models.Model):
    section = models.ForeignKey("course_app.Section", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name="transcript")
    grade = models.IntegerField()

    class Meta:
        unique_together = ('section', 'student')