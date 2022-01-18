from django.urls import path
from .views import (
    DeleteHarajatlar,
    Home,
    Subjects, 
    Students, 
    Teachers,
    RegisterHome,
    TeachersList,
    StudentsList,
    DeleteSubject,
    DeleteTeacher,
    DeleteStudent,
    AddSubjectView,
    AddStudentView,
    AddTeacherView,
    SubjectUpdateView,
    TeacherUpdateView,
    StudentUpdateView,
    PaymentList,
    DeletePayment,
    AddPaymentView,
    PaymentUpdateView,
    Pass_year,
    This_year,
    This_month,
    ReportSection,
    HarajatlarView,
    UpdateHarajatlar,
    DeleteHarajatlar,
)

app_name = 'app'

urlpatterns = [
    path("", Home, name="Home"),
    path("subject/", Subjects, name="Subject"),
    path("payment/pass_year/", Pass_year, name="PassYear"),
    path("payment/this_year/", This_year, name="ThisYear"),
    path("payment/this_month/", This_month, name="ThisMonth"),
    path("tea/<id_sub>/", Teachers, name="Teacher"),
    path("stu/<id_tea>/", Students, name="Student"),
    path("report/", ReportSection, name="ReportSection"),
    path("register_home/", RegisterHome, name="RegisterHome"),
    path("payment/", PaymentList.as_view(), name="PaymentHome"),
    path("all/teachers/", TeachersList.as_view(), name="TeacherList"),
    path("all/students/", StudentsList.as_view(), name="StudentList"),
    path("delete/subject/<pk>/", DeleteSubject.as_view(), name="DeleteSubject"),
    path("delete/teacher/<pk>/", DeleteTeacher.as_view(), name="DeleteTeacher"),
    path("delete/student/<pk>/", DeleteStudent.as_view(), name="DeleteStudent"),
    path("delete/payment/<pk>/", DeletePayment.as_view(), name="DeletePayment"),
    path("delete/harajat/<pk>/", DeleteHarajatlar.as_view(), name="DeleteHarajatlar"),
    path("update/subject/<pk>/", SubjectUpdateView.as_view(), name="UpdateSubject"),
    path("update/teacher/<pk>/", TeacherUpdateView.as_view(), name="UpdateTeacher"),
    path("update/student/<pk>/", StudentUpdateView.as_view(), name="UpdateStudent"),
    path("update/payment/<pk>/", PaymentUpdateView.as_view(), name="UpdatePayment"),
    path("update/harajat/<pk>/", UpdateHarajatlar.as_view(), name="UpdateHarajatlar"),
    path("register_home/subject/", AddSubjectView.as_view(), name="RegisterSubject"),
    path("register_home/teacher/", AddTeacherView.as_view(), name="RegisterTeacher"),
    path("register_home/student/", AddStudentView.as_view(), name="RegisterStudent"),
    path("payment/add_payment/", AddPaymentView.as_view(), name="RegisterPayment"),
    path("harajatlar/add/", HarajatlarView.as_view(), name="RegisterHarajatlar"),
]
