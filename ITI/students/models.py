from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    class_year = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    courses = models.ManyToManyField('courses.Course', related_name='students')
    photo = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.name