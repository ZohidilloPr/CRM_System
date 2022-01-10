from django.urls import path
from .views import RegisterCreateView, LogIn

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="RGU"),
    path("login/", LogIn, name='LIU')
]