from django.shortcuts import redirect, render
from .models import (
    Subject, 
    Teacher, 
    Student,
    Payment,
)
from .forms import SubjectForm, TeacherForm, StudentForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# Create your views here.

def Home(request):
    """Asosiy bolim"""
    return render(request, 'home.html')

def Subjects(request):
    """Centerdagi hamma fanlar"""
    sub = Subject.objects.all()
    return render(request, 'sections/subjects.html', {'sub':sub})

def Teachers(request, id_sub):
    """Fanga aloqador o'qituvchilar"""
    tea = Teacher.objects.filter(subject=id_sub)
    context = {
        'tea':tea,
        'id_sub':id_sub,
    }
    return render(request, 'sections/teachers.html', context)

def Students(request, id_tea):
    """O'qituvchilarning o'quvchilari"""
    stu = Student.objects.filter(teacher=id_tea)
    context = {
        'stu':stu,
        'id_tea':id_tea,
    }
    return render(request, 'sections/students.html', context)

class TeachersList(ListView):
    """Hamma o'qituvchilarni ro'yhati"""
    model = Teacher
    template_name = 'coworkers/workers.html'
    ordering = '-registred_time'
    paginate_by = 5

# Register bolimi

def RegisterHome(request):
    """Asosiy Register Bo'limi"""
    return render(request, 'register/register_home.html')

# centerda o'tiladigan fanlar uchun
class AddSubjectView(CreateView):
    """Yangi fan qo'shish"""
    model = Subject
    template_name = 'register/subject_form.html'
    fields = '__all__'

class SubjectUpdateView(UpdateView):
    """Fanni taxrirlash"""
    model = Subject
    template_name = "update/subject_update.html"
    fields = '__all__'

class DeleteSubject(DeleteView):
    """O'chirish"""
    model = Subject
    success_url = '/subject/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# centerda ishlaydigan o'qituvchilar uchun

class AddTeacherView(CreateView):
    """Yangi o'qituvchisi qo'shish"""
    model = Teacher
    template_name = 'register/teacher_form.html'
    fields = '__all__'

class TeacherUpdateView(UpdateView):
    """O'qituvchini Taxrirlash"""
    model = Teacher
    template_name = 'update/teacher_update.html'
    fields = '__all__'

class DeleteTeacher(DeleteView):
    """O'chirish"""
    model = Teacher
    success_url = '/subject/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AddStudentView(CreateView):
    """Yangi Talaba qo'shish"""
    model = Student
    template_name = 'register/student_form.html'
    fields = '__all__'

class StudentUpdateView(UpdateView):
    """Talabani Taxrirlash"""
    model = Student
    template_name = 'update/student_update.html'
    fields = '__all__'

class DeleteStudent(DeleteView):
    """O'chirish"""
    model = Student
    success_url = '/subject/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Payment Sections
def Payment(request):
    pay = Payment.objects.all().order('-payed_date')
    return render(request, 'payment/payment_home.hmtl', {'pay':pay})
