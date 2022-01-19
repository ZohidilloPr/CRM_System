from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

"""Talabaning qaysi kunlari o'qishga Borishi"""
study_days = (
    ('du-ch-j', 'Du-Ch-J'),
    ('se-p-sh', 'Se-P-Sh'),
    ('du-se-ch-p-j', 'Du-Se-Ch-P-J'),
    ('har kunlik', 'Har Kunlik'),
    ('option', 'Option')
)
"""Talabaning o'qish turi"""
study_type = (
    ('team', 'Team'),
    ('induvidual', 'Induvidual'),
    ('option', 'Option')
)

class Subject(models.Model):
    """Centerda o'qitiladigan fanlar"""
    name =models.CharField(_("Fan nomi"), max_length=100)
    added_date = models.DateTimeField(_("qoshilgan fani"), auto_now_add=True)

    def __str__(self):
        return self.name

    """Bitta fan uchun shu oyda qancha tolanganligini ko'rsatadi"""
    @property
    def this_month_payment(self):
        oy = int(datetime.now().month)
        payment = self.payment_set.all()
        this_month = []
        for i in payment:
            if i.payed_date.month == oy:
                this_month.append(i)
        total = sum([i.payment for i in this_month])
        return total        

    """Bitta fanda nechta o'qituvchi borligini ko'rsatadi"""
    @property
    def self_teachers(self):
        tea = self.teacher_set.all().count()
        return tea
    
    """Bitta fanda nechta o'quvchi borligini ko'rsatadi"""
    @property
    def self_students(self):
        student = self.student_set.all().count()
        return student

class Teacher(models.Model):
    """Centerda ishlaydigan o'qituvchilar"""
    f_name = models.CharField(_("To'liq ismi"), max_length=100)
    subject = models.ForeignKey(Subject, verbose_name=_("O'qitadigan fani"), on_delete=models.CASCADE)
    address = models.CharField(_("Manzil"), max_length=100)
    phone_num = models.CharField(_("Telefon raqami"), max_length=9)
    registred_time = models.DateTimeField(_("royhatga olingan vaqt"), auto_now_add=True)

    def __str__(self):
        return f'{self.f_name} from {self.subject.name}'
    
    """Bitta fan uchun shu oyda qancha tolanganligini ko'rsatadi"""
    @property
    def this_month_payment(self):
        oy = int(datetime.now().month)
        payment = self.payment_set.all()
        this_month = []
        for i in payment:
            if i.payed_date.month == oy:
                this_month.append(i)
        total = sum([i.payment for i in this_month])
        return total 

    """Bitta o'qituvchi qancha oylik olishligini ko'rsatadi"""
    @property
    def salary(self):
        total = self.this_month_payment / 2
        return total

    """Hamma o'qituvchi qancha olishligini ko'rsatadi"""
    @property
    def get_total_salary(self):
        teacher = Teacher.objects.all()
        total = sum([i.salary for i in teacher])
        return total

    """Bitta O'qituvchida nechta o'quvchi borligini ko'rsatadi"""
    @property
    def self_students(self):
        student = self.student_set.all().count()
        return student
    


class Student(models.Model):
    """Centerda o'qiydigan o'quvchilar"""
    f_name = models.CharField(_("To'liq ismi"), max_length=100)
    subject = models.ForeignKey(Subject, verbose_name=_("O'rganadigan fani"), on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name=_("O'qituvchisi"), on_delete=models.CASCADE)
    phone_num = models.CharField(_("Telefon raqami"), max_length=9)
    study_days = models.CharField(_("O'qish Kunlari"), max_length=50, choices=study_days, default='option')
    study_type = models.CharField(_("O'qish turi"), max_length=50, choices=study_type, default='option')
    registered_date = models.DateTimeField(_("Ro'yhatga olingan vaqti"), auto_now_add=True)

    def __str__(self):
        return f'{self.f_name} from {self.subject.name}'
 
    """Bitta student shu oyda necha pul tolov qilganligini ko'rsatadi"""
    @property
    def this_month_pay(self):
        oy = int(datetime.now().month)
        pay = self.payment_set.all()
        this_month = []
        for i in pay:
            if i.payed_date.month == oy:
                this_month.append(i)
        total = sum([i.payment for i in this_month])
        return total
        
class Payment(models.Model):
    """O'quvchilarning Tolovlari"""
    student = models.ForeignKey(Student, verbose_name=_("Talaba"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name=_("Qaysi fan uchun"), on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name=_("O'qituvchisi"), on_delete=models.CASCADE, null=True, blank=True)
    payment = models.IntegerField(_("Tolov summasi"), default=0)
    payed_date = models.DateTimeField(_("To'langan vaqt"), auto_now_add=True)

    def __str__(self):
        return f'{self.student.f_name} {self.payment} so\'m'

    """To'langan umumiy summa olish"""
    @property
    def get_total_payment(self):
        pay = Payment.objects.all()
        total = sum([i.payment for i in pay])
        return total
    
    """O'qituvchilarga To'lanadigan umumiy summa"""
    @property
    def get_total_salary(self):
        total = self.get_total_payment / 2
        return total
    
    """Centerning umumiy harajatlari"""
    @property
    def get_total_outlay(self):
        """Umumiy harajatlar"""
        outlay = Harajatlar.objects.all()
        total = sum([i.amount for i in outlay])
        return total

    """Centerga qoladigan soft foyda"""
    @property
    def total_benifet(self):
        total = self.get_total_salary - self.get_total_outlay
        return total

# HARAJATLAR
class Harajatlar(models.Model):
    """Centerning Harajatlari"""
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    name = models.CharField(_("Nima uchun"), max_length=100)
    amount = models.IntegerField(_("Qancha miqdorda"), default=0)
    used_date = models.DateTimeField(_("Ishlatilgan vaqti"), auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_total_outlay(self):
        """Umumiy harajatlar"""
        outlay = Harajatlar.objects.all()
        total = sum([i.amount for i in outlay])
        return total

