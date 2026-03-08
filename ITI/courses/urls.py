from django.urls import path
from .views import list_courses, add_course, show_course_detail

urlpatterns = [
    path('' , list_courses, name='list_courses'),
    path('add_course/', add_course, name='add_course'),
    path('<int:course_id>/', show_course_detail, name='course_detail'),
]   
