from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class RegisterUser(forms.ModelForm):

    password = forms.CharField(label='PASSWORD', widget=forms.PasswordInput())
    password2 = forms.CharField(label='PASSWORDni Tasdiqlash', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','phone_number','email')

    def clean_email(self):
        
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Bu email Band')
        return email
    
    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password is not None and password != password2:
            raise forms.ValidationError('password2 da hato qaytadan tekshiring!')
        return cleaned_data    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Passwordni Tasdiqlash', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email',)

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password is not None and password != password2:
            raise forms.ValidationError('password2 da hato qaytadan tekshiring!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'admin')

    def clean_password(self):
        return self.initial['password']

