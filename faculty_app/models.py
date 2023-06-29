from django.db import models
from person_app.models import Person
from student_app.models import Student, Grade_Student
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

@receiver(post_save, sender=Faculty)
def insert_faculty_as_instructor(sender, instance, **kwargs):
    instructor_type = ContentType.objects.get_for_model(Faculty)
    instructor_ssn = instance.ssn

    Instructor_Researcher.objects.get_or_create(
        instructor_type=instructor_type,
        instructor_ssn=instructor_ssn,
    )
    
@receiver(post_save, sender=Grade_Student)
def insert_grad_student_as_instructor_researcher(sender, instance, **kwargs):
    instructor_type = ContentType.objects.get_for_model(Grade_Student)
    instructor_ssn = instance.student.ssn

    Instructor_Researcher.objects.get_or_create(
        instructor_type=instructor_type,
        instructor_ssn=instructor_ssn,
    )
    
class Instructor_Researcher(models.Model):
    instructor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    instructor_ssn = models.CharField(max_length=15)
    instructor = GenericForeignKey("instructor_type", "instructor_ssn")

    def __str__(self):
        return f"{self.instructor_ssn}"
    
@receiver(post_save, sender=Instructor_Researcher)
def pr(sender, instance, **kwargs):
    print(instance)

