from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# import datetime

# Create your models here.


class UserProfileManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(
        self,
        email,
        full_name,
        password=None
        # , birthday=datetime.date(2002, 3, 11)
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
            # , birthday=birthday
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(
        self,
        email,
        full_name,
        password=None
        # birthday=datetime.date(2002, 3, 11)
    ):
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name
            # , birthday=birthday
        )
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        full_name,
        password=None
        # , birthday=datetime.date(2002, 3, 11)
    ):
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            # , birthday=birthday
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):
    """
    Creates a customized database table for user using customized user manager
    """

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(
        ("full_name"),
        max_length=150,
        null=True,
        blank=True,
    )
    # birthday = (models.DateField(default=datetime.date(2002, 3, 11)),)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserProfileManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# source venv/bin/activate
