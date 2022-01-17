from django.contrib import admin
from .models import Subject, Teacher, Student, Payment

# Register your models here.

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Payment)