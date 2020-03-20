from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class StudentDetails(models.Model):

    name = models.CharField(max_length=50,null=True)
    fname = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    qualification = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    phoneno = models.CharField(max_length=12,null=True)

    def __str__(self):
        return self.name
