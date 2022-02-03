from django.urls import path
from .views import (
    Home,
    Subjects, 
    Students, 
    Teachers,
    Pass_year,
    This_year,
    Arxiv_Home,
    This_month,
    PaymentList,
    TeachersList,
    StudentsList,
    RegisterHome,
    Arxiv_Harajat,
    Arxiv_Student,
    Arxiv_teacher,
    SearchPayment,
    DeleteSubject,
    DeleteTeacher,
    DeleteStudent,
    ReportSection,
    SearchTeacher,
    DeletePayment,
    AddSubjectView,
    AddStudentView,
    AddTeacherView,
    AddPaymentView,
    SearchStudents,
    HarajatlarView,
    look_sertificate,
    DeleteHarajatlar,
    UpdateHarajatlar,
    DeleteHarajatlar,
    SubjectUpdateView,
    TeacherUpdateView,
    StudentUpdateView,
    PaymentUpdateView,
)

app_name = 'app'

urlpatterns = [
    path("", Home, name="Home"),
    path("arxiv/", Arxiv_Home, name="Arxiv"),
    path("subject/", Subjects, name="Subject"),
    path("tea/<id_sub>/", Teachers, name="Teacher"),
    path("stu/<id_tea>/", Students, name="Student"),
    path("report/", ReportSection, name="ReportSection"),
    path("payment/pass_year/", Pass_year, name="PassYear"),
    path("payment/this_year/", This_year, name="ThisYear"),
    path("arxiv/salary/", Arxiv_teacher, name="AllTeacher"),
    path("arxiv/payment/", Arxiv_Student, name="AllPayment"),
    path("arxiv/harajat/", Arxiv_Harajat, name="AllHarajat"),
    path("payment/this_month/", This_month, name="ThisMonth"),
    path("register_home/", RegisterHome, name="RegisterHome"),
    path("payment/", PaymentList.as_view(), name="PaymentHome"),
    path("all/teachers/", TeachersList.as_view(), name="TeacherList"),
    path("all/students/", StudentsList.as_view(), name="StudentList"),
    path("one/teacher/<pk>/", look_sertificate.as_view(), name="resume"),
    path("search/teacher/", SearchTeacher.as_view(), name="SearchTeacher"),
    path("search/payment/", SearchPayment.as_view(), name="SearchPayment"),
    path("search/student/", SearchStudents.as_view(), name="SearchStudent"),
    path("delete/subject/<pk>/", DeleteSubject.as_view(), name="DeleteSubject"),
    path("delete/teacher/<pk>/", DeleteTeacher.as_view(), name="DeleteTeacher"),
    path("delete/student/<pk>/", DeleteStudent.as_view(), name="DeleteStudent"),
    path("delete/payment/<pk>/", DeletePayment.as_view(), name="DeletePayment"),
    path("harajatlar/add/", HarajatlarView.as_view(), name="RegisterHarajatlar"),
    path("payment/add_payment/", AddPaymentView.as_view(), name="RegisterPayment"),
    path("update/subject/<pk>/", SubjectUpdateView.as_view(), name="UpdateSubject"),
    path("update/teacher/<pk>/", TeacherUpdateView.as_view(), name="UpdateTeacher"),
    path("update/student/<pk>/", StudentUpdateView.as_view(), name="UpdateStudent"),
    path("update/payment/<pk>/", PaymentUpdateView.as_view(), name="UpdatePayment"),
    path("register_home/subject/", AddSubjectView.as_view(), name="RegisterSubject"),
    path("register_home/teacher/", AddTeacherView.as_view(), name="RegisterTeacher"),
    path("register_home/student/", AddStudentView.as_view(), name="RegisterStudent"),
    path("update/harajat/<pk>/", UpdateHarajatlar.as_view(), name="UpdateHarajatlar"),
    path("delete/harajat/<pk>/", DeleteHarajatlar.as_view(), name="DeleteHarajatlar"),
]
