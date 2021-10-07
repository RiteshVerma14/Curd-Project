from django.db import models

# Create your models here.

class add_new_student(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name