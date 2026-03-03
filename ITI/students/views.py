from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_students(request):

    students = [
        {"name": "Ahmed", "age": 23, "department": "AI", "class": "2025"},
        {"name": "Basma", "age": 22, "department": "CS", "class": "2025"},
        {"name": "Ali", "age": 24, "department": "DS", "class": "2025"},
        {"name": "Sara", "age": 21, "department": "SE", "class": "2024"},
        {"name": "Omar", "age": 25, "department": "IT", "class": "2025"},
        {"name": "Nour", "age": 22, "department": "AI", "class": "2024"},
        {"name": "Khaled", "age": 23, "department": "CS", "class": "2023"},
        {"name": "Mariam", "age": 21, "department": "IS", "class": "2026"},
        {"name": "Youssef", "age": 24, "department": "DS", "class": "2024"},
        {"name": "Fatima", "age": 20, "department": "SE", "class": "2026"},
        {"name": "Hassan", "age": 26, "department": "IT", "class": "2023"},
        {"name": "Laila", "age": 22, "department": "AI", "class": "2026"},
        {"name": "Tarek", "age": 23, "department": "IS", "class": "2025"},
        {"name": "Dina", "age": 21, "department": "CS", "class": "2024"},
        {"name": "Karim", "age": 25, "department": "DS", "class": "2023"},
    ]

    selected_class = request.GET.get("class", "All")
    selected_department = request.GET.get("department", "All")
    name_search = request.GET.get("name", "")

    results = students
    if selected_class != "All":
        results = [student for student in results if student["class"] == selected_class]

    if selected_department != "All":
        results = [student for student in results if student["department"] == selected_department]

    if name_search:
        results = [student for student in results if name_search.lower() in student["name"].lower()]

    context = {
        "students": results,
        "SelectedClass": selected_class,
        "SelectedDepartment": selected_department,
        "NameSearch": name_search
    }

    return render(request, 'base.html', context=context)



def show_student(request, name):
    return HttpResponse(f"Student: {name}")