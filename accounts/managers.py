from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ Create a user """

        if not email:
            return ValueError({'email': 'email field required'})

        email = self.normalize_email(email)
        validate_password(password)

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password=None,**extra_fields):

        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if not email:
            return ValueError({'email': 'email field required'})

        email = self.normalize_email(email)
        validate_password(password)

        superuser = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        superuser.save()
        return superuser
