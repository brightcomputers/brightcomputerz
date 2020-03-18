from django.contrib import admin
from student import models
from .models import StudentDetails


admin.site.register(StudentDetails)
