from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from staff.models import Instructor


def list_courses(request):
    courses = Course.objects.select_related('instructor').all()
    name_search = request.GET.get('name', '')
    selected_instructor = request.GET.get('instructor', '')
    selected_credits = request.GET.get('credits', '')

    if name_search:
        courses = courses.filter(name__icontains=name_search)
    if selected_instructor:
        courses = courses.filter(instructor__pk=selected_instructor)
    if selected_credits:
        courses = courses.filter(credits=selected_credits)

    instructors = Instructor.objects.all()
    all_credits = sorted(set(Course.objects.values_list('credits', flat=True)))

    return render(request, 'courses/list.html', {
        'courses': courses,
        'name_search': name_search,
        'selected_instructor': selected_instructor,
        'selected_credits': selected_credits,
        'instructors': instructors,
        'all_credits': all_credits,
    })


def show_course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    return render(request, 'courses/detail.html', {
        'course': course,
        'students': students,
    })


def add_course(request):
    instructors = Instructor.objects.all()
    if request.method == 'POST':
        instructor_id = request.POST.get('instructor') or None
        Course.objects.create(
            name=request.POST['name'],
            code=request.POST['code'],
            description=request.POST['description'],
            credits=request.POST['credits'],
            instructor_id=instructor_id,
        )
        return redirect('list_courses')
    return render(request, 'courses/add.html', {'instructors': instructors})

