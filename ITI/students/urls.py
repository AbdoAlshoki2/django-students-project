from django.urls import path
from students.views import list_students, show_student

urlpatterns = [
    path('', list_students, name='show_students'),
    path('<str:name>/', show_student, name='show_student'),
]