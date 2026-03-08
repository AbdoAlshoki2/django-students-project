from django.shortcuts import render
from students.models import Student
from courses.models import Course
from staff.models import Instructor


def home(request):
    return render(request, 'home.html', {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'instructor_count': Instructor.objects.count(),
    })
