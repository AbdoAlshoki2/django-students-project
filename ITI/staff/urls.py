from django.urls import path
from staff.views import list_instructors, show_instructor, add_instructor

urlpatterns = [
    path('', list_instructors, name='list_instructors'),
    path('add/', add_instructor, name='add_instructor'),
    path('<int:pk>/', show_instructor, name='show_instructor'),
]