from django.db import models
from person_app.models import Person
from student_app.models import Student, Grad_Student
from rest_framework.serializers import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save

class Faculty(Person):
    rank = models.IntegerField()
    f_office = models.IntegerField()
    f_phone = models.CharField(max_length=15)
    salary = models.PositiveIntegerField()
    departments = models.ManyToManyField("college_app.Department", related_name="facul")

@receiver(post_save, sender=Faculty)
def insert_faculty_as_instructor(sender, instance, **kwargs):
    instructor_type = ContentType.objects.get_for_model(Faculty)
    instructor_ssn = instance.ssn

    Instructor_Researcher.objects.get_or_create(
        instructor_type=instructor_type,
        instructor_ssn=instructor_ssn,
    )
    
@receiver(post_save, sender=Grad_Student)
def insert_grad_student_as_instructor_researcher(sender, instance, **kwargs):
    instructor_type = ContentType.objects.get_for_model(Grad_Student)
    instructor_ssn = instance.student.ssn

    Instructor_Researcher.objects.get_or_create(
        instructor_type=instructor_type,
        instructor_ssn=instructor_ssn,
    )
    
class Instructor_Researcher(models.Model):
    instructor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    instructor_ssn = models.CharField(max_length=15, primary_key=True)
    instructor = GenericForeignKey("instructor_type", "instructor_ssn")

    def __str__(self):
        ## TODO: Fix this shit to return the instructor instead of instructor_ssn, the proplem is it returns None in case of Grad Student
        return f"{self.instructor_ssn}"
    

class Grant(models.Model):
    title = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    start_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="pl")

    def __str__(self):
        return f"{self.id}: {self.title} | {self.faculty}"


class Support(models.Model):
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name="supports")
    instructor_researcher = models.ForeignKey(Instructor_Researcher, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    time = models.IntegerField()