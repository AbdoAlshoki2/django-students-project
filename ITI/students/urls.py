from django.urls import path
from students.views import list_students, show_student, add_student

urlpatterns = [
    path('', list_students, name='show_students'),
    path('add/', add_student, name='add_student'),
    path('<int:pk>/', show_student, name='show_student'),
]