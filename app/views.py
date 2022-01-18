from django.shortcuts import redirect, render
from datetime import datetime
from .models import (
    Subject, 
    Teacher, 
    Student,
    Payment,
    Harajatlar,
)
from .forms import SubjectForm, TeacherForm, StudentForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
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

class StudentsList(ListView):
    """Hamma o'quvchilarni ro'yhati"""
    model = Student
    template_name = 'all/all_students.html'
    ordering = '-registered_date'
    paginate_by = 5

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
    success_url = '/register_home/subject/'


class SubjectUpdateView(UpdateView):
    """Fanni taxrirlash"""
    model = Subject
    template_name = "update/subject_update.html"
    fields = '__all__'
    success_url = '/subject/'


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
    success_url = '/all/teachers/'


class TeacherUpdateView(UpdateView):
    """O'qituvchini Taxrirlash"""
    model = Teacher
    template_name = 'update/teacher_update.html'
    fields = '__all__'
    success_url = '/all/teachers/'


class DeleteTeacher(DeleteView):
    """O'chirish"""
    model = Teacher
    success_url = '/all/teachers/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AddStudentView(CreateView):
    """Yangi Talaba qo'shish"""
    model = Student
    template_name = 'register/student_form.html'
    fields = '__all__'
    success_url = '/all/students/'


class StudentUpdateView(UpdateView):
    """Talabani Taxrirlash"""
    model = Student
    template_name = 'update/student_update.html'
    fields = '__all__'
    success_url = '/all/students/'
    

class DeleteStudent(DeleteView):
    """O'chirish"""
    model = Student
    success_url = '/subject/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Payment Sections

class PaymentList(ListView):
    model = Payment
    template_name = "payment/payment_home.html"
    ordering = '-payed_date'
    paginate_by = 5

class AddPaymentView(CreateView):
    """Yangi Payment qo'shish"""
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = '__all__'
    success_url = '/payment/'


class PaymentUpdateView(UpdateView):
    """Payment Taxrirlash"""
    model = Payment
    template_name = 'payment/payment_update.html'
    fields = '__all__'
    success_url = '/payment/'


class DeletePayment(DeleteView):
    """O'chirish"""
    model = Payment
    success_url = '/payment/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Filter section

def Pass_year(request):
    pass_year = int(datetime.now().year) - 1
    pay = Payment.objects.all()
    pass_year_list = []
    for i in pay:
        if i.payed_date.year == pass_year:
            pass_year_list.append(i)
    paginator = Paginator(pass_year_list, 10) # Show 10 list per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'object_list':pass_year_list,
    }
    return render(request, 'payment/payment_history/payment_history_pass_year.html', context)

def This_year(request):
    this_year = int(datetime.now().year)
    pay = Payment.objects.all()
    this_year_list = []
    for i in pay:
        if i.payed_date.year == this_year:
            this_year_list.append(i)
    paginator = Paginator(this_year_list, 10) # Show 10 list per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'object_list':this_year_list,
    }
    return render(request, 'payment/payment_history/payment_history_this_year.html', context)

def This_month(request):
    this_month = int(datetime.now().month)
    pay = Payment.objects.all()
    this_month_list = []
    for i in pay:
        if i.payed_date.month == this_month:
            this_month_list.append(i)
    
    paginator = Paginator(this_month_list, 10) # Show 10 list per page.

    number = request.GET.get('page')
    page_obj = paginator.get_page(number)
    context = {
        'page_obj':page_obj,
        'object_list':this_month_list,
    }
    return render(request, 'payment/payment_history/this_month.html', context)

def ReportSection(request):
    subject = Subject.objects.all().count()
    teacher = Teacher.objects.all().count()
    student = Student.objects.all().count()

    payment = Payment.objects.all()

    context = {
        'subject': subject,
        'teacher': teacher,
        'student': student,
        'payment':payment,
    }
    return render(request, 'report_section/report_home.html', context)

class HarajatlarView(CreateView):
    """Harajatlar qo'shish"""
    model = Harajatlar
    template_name = "report_section/total_outlies.html"
    fields = '__all__'
    success_url = '/harajatlar/add/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Harajatlar.objects.all()
        return super().get_context_data(**kwargs)

class UpdateHarajatlar(UpdateView):
    """Harajatlar taxrirlash"""
    model = Harajatlar
    template_name = "report_section/outlies_update.html"
    fields = '__all__'
    success_url = 'harajatlar/add/'

class DeleteHarajatlar(DeleteView):
    """Harajatlar o'chirib yuborish"""
    model = Harajatlar
    success_url = '/harajatlar/add/'