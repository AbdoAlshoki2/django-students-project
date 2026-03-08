from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def list_students(request):
    students = Student.objects.all()
    name_search = request.GET.get('name', '')
    selected_department = request.GET.get('department', '')
    selected_class_year = request.GET.get('class_year', '')

    if name_search:
        students = students.filter(name__icontains=name_search)
    if selected_department:
        students = students.filter(department=selected_department)
    if selected_class_year:
        students = students.filter(class_year=selected_class_year)

    all_students = Student.objects.all()
    departments = sorted(set(all_students.values_list('department', flat=True)))
    class_years = sorted(set(all_students.values_list('class_year', flat=True)))

    return render(request, 'students/list.html', {
        'students': students,
        'name_search': name_search,
        'selected_department': selected_department,
        'selected_class_year': selected_class_year,
        'departments': departments,
        'class_years': class_years,
    })


def show_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    courses = student.courses.select_related('instructor').all()
    return render(request, 'students/detail.html', {
        'student': student,
        'courses': courses,
    })


def add_student(request):
    if request.method == 'POST':
        student = Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            class_year=request.POST['class_year'],
            enrollment_date=request.POST['enrollment_date'],
        )
        if request.FILES.get('photo'):
            student.photo = request.FILES['photo']
            student.save()
        return redirect('show_students')
    return render(request, 'students/add.html')
