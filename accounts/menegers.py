from django.contrib.auth.models import BaseUserManager

class CustomUserManeger(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Emailni kiritishingiz kerak!')
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_staffuser(self, email, password, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user