from django import forms
from .models import Subject, Teacher, Student

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('f_name', 'subject', 'address', 'phone_num',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('f_name', 'subject', 'teacher', 'study_days', 'study_type', 'phone_num',)

