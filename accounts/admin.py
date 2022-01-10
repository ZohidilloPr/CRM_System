from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()
# Register your models here.

admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User
    
    list_display = ('email','first_name', 'last_name', 'phone_number', 'admin',)
    list_filter = ('first_name', 'last_name', 'phone_number', 'email', 'admin', 'staff', 'is_active',)

    fieldsets = (
        (None, {
            "fields": (
                'first_name', 'last_name','phone_number','email','password',
            ),
        }),
        ('Permissions', {
            "fields":(
                'is_active', 'staff', 'admin',
            )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('email', 'password', 'password2', 'staff', 'is_active', 'admin')
        }),
    )
    search_fields = ('email', 'phone_number',)
    ordering = ('-joined_date',)

admin.site.register(User, CustomUserAdmin)
    
