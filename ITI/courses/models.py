from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    credits = models.IntegerField()
    instructor = models.ForeignKey('staff.Instructor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
