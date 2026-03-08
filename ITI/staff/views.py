from django.shortcuts import render, get_object_or_404, redirect
from .models import Instructor


def list_instructors(request):
    instructors = Instructor.objects.all()
    name_search = request.GET.get('name', '')
    selected_department = request.GET.get('department', '')

    if name_search:
        instructors = instructors.filter(name__icontains=name_search)
    if selected_department:
        instructors = instructors.filter(department=selected_department)

    departments = sorted(set(Instructor.objects.values_list('department', flat=True)))

    return render(request, 'staff/list.html', {
        'instructors': instructors,
        'name_search': name_search,
        'selected_department': selected_department,
        'departments': departments,
    })


def show_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    courses = instructor.course_set.all()
    return render(request, 'staff/detail.html', {
        'instructor': instructor,
        'courses': courses,
    })


def add_instructor(request):
    if request.method == 'POST':
        instructor = Instructor.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
        )
        if request.FILES.get('photo'):
            instructor.photo = request.FILES['photo']
            instructor.save()
        return redirect('list_instructors')
    return render(request, 'staff/add.html')

