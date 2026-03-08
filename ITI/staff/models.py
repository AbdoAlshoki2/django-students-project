from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/', null=True, blank=True)

    def __str__(self):
        return self.name