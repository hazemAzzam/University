from django.db import models

# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=50, primary_key=True)
    dean = models.CharField(max_length=50)
    college_office = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.college_name}"

class Department(models.Model):
    name = models.CharField(max_length=50, primary_key=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    office = models.CharField(max_length=50, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="departments", blank=True)
    chairs = models.OneToOneField("faculty_app.Faculty", on_delete=models.CASCADE, related_name="chairs", blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.college}"