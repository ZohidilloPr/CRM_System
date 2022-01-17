from django import urls
from django.urls import path
from .views import (
    Home,
    Subjects, 
    Students, 
    Teachers,
    RegisterHome,
    TeachersList,
    DeleteSubject,
    DeleteTeacher,
    DeleteStudent,
    AddSubjectView,
    AddStudentView,
    AddTeacherView,
    SubjectUpdateView,
    TeacherUpdateView,
    StudentUpdateView,
)

app_name = 'app'

urlpatterns = [
    path("", Home, name="Home"),
    path("subject/", Subjects, name="Subject"),
    path("tea/<id_sub>/", Teachers, name="Teacher"),
    path("stu/<id_tea>/", Students, name="Student"),
    path("register_home/", RegisterHome, name="RegisterHome"),
    path("all/teachers/", TeachersList.as_view(), name="TeacherList"),
    path("delete/subject/<pk>/", DeleteSubject.as_view(), name="DeleteSubject"),
    path("delete/teacher/<pk>/", DeleteTeacher.as_view(), name="DeleteTeacher"),
    path("delete/student/<pk>/", DeleteStudent.as_view(), name="DeleteStudent"),
    path("update/subject/<pk>/", SubjectUpdateView.as_view(), name="UpdateSubject"),
    path("update/teacher/<pk>/", TeacherUpdateView.as_view(), name="UpdateTeacher"),
    path("update/student/<pk>/", StudentUpdateView.as_view(), name="UpdateStudent"),
    path("register_home/subject/", AddSubjectView.as_view(), name="RegisterSubject"),
    path("register_home/teacher/", AddTeacherView.as_view(), name="RegisterTeacher"),
    path("register_home/student/", AddStudentView.as_view(), name="RegisterStudent"),
]
