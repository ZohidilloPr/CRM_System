from django.urls import path
from .views import RegisterCreateView, LogIn, Logot

app_name = 'accounts'

urlpatterns = [
    path("", LogIn, name='LIU'),
    path("chiqish/", Logot, name='OUT'),
]