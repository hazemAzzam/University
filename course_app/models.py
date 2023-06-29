from django.db import models

# Create your models here.
class Course(models.Model):
    course_number = models.CharField(max_length=6, primary_key=True)
    course_name = models.CharField(max_length=50)
    course_desc = models.TextField()
    department = models.ForeignKey("college_app.Department", on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.course_name}"

class Section(models.Model):
    number = models.CharField(max_length=5, primary_key=True)
    year = models.IntegerField()
    qtr = models.CharField(choices=[
        ("Fall", "Fall"),
        ("Winter", "Winter"),
        ("Spring", "Spring"),
        ("Summer", 'Summer')
    ], max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    instructor_researcher = models.ForeignKey("faculty_app.Instructor_Researcher", on_delete=models.SET_NULL, null=True, related_name="teach")



