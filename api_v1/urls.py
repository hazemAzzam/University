from django.urls import path, include
from rest_framework.routers import DefaultRouter
from person_app.views import *
from student_app.views import *
from faculty_app.views import *
from course_app.views import *
from college_app.views import *
router = DefaultRouter()

router.register('students', Student_View)
router.register('faculities', Faculty_View)
router.register('grade_students', Grad_Student_View)
#router.register('instructor-researchers', Instructor_Researcher_View)
router.register('instructor-researchers', Instructor_Researcher_V2_View)
router.register('transcript', Transcript_View)

router.register('request-open-course', Register_View)

router.register('sections', Section_View, basename='sections')
router.register('course-registerations', Register_View, basename='register')

router.register('grants', Grant_View)
router.register('supports', Support_View)

router.register('courses', Course_View)

router.register('colleges', College_View)
router.register('departments', Department_View)

urlpatterns = [
    path('', include(router.urls))
]