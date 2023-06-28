from django.db import models

# Create your models here.
class Section(models.Model):
    number = models.CharField(max_length=5, primary_key=True)
    year = models.IntegerField()
    qtr = models.CharField(choices=[
        ("Fall", "Fall"),
        ("Winter", "Winter"),
        ("Spring", "Spring"),
        ("Summer", 'Summer')
    ], max_length=15)
    instructor_researcher = models.ForeignKey("faculty_app.Instructor_Researcher", on_delete=models.SET_NULL, null=True, related_name="teach")



