from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.OneToOneField("Name", on_delete=models.CASCADE)
    
    @property
    def full_name(self):
        return f"{self.name.fname} {self.name.minit} {self.name.lname}"
    
    ssn = models.CharField(max_length=15, primary_key=True)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=12, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])

    address= models.OneToOneField("Address", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name}"


class Name(models.Model):
    fname = models.CharField(max_length=50, null=False, blank=False)
    minit = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.minit} {self.lname}"

class Address(models.Model):
    no = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    apt_no = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    