from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission
)
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField
from .company import Company
from .team import Team
from .university import University
from .research_institution import ResearchInstitution
from .health_institution import HealthInstitution



class UserRole(models.TextChoices):
    INDIVIDUAL = "individual", "Individual User"
    TEAM_MEMBER = "team_member", "Team Member"
    COMPANY = "company", "Company User"
    STUDENT = "student", "Student"
    TEACHER = "teacher", "Teacher"
    UNIVERSITY = "university", "University Staff"
    RESEARCH_INSTITUTION = "research_institution", "Research Institution"
    HEALTH = "health", "Health / Hospital"
    ADMIN = "admin", "Admin"
    SUPERADMIN = "superadmin", "Super Admin"



class UserStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    SUSPENDED = "suspended", "Suspended"


class ETLUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=UserRole.INDIVIDUAL, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", UserRole.SUPERADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email=email, password=password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        Group, blank=True, related_name="etl_user_groups"
    )
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="etl_user_permissions"
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=UserRole.choices, default=UserRole.INDIVIDUAL)
    status = models.CharField(max_length=10, choices=UserStatus.choices, default=UserStatus.ACTIVE)

    slug = AutoSlugField(populate_from='email', unique=True, always_update=False)

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="team_members"
    )
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    research_institution = models.ForeignKey(
        ResearchInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    health_institution = models.ForeignKey(
        HealthInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    profile_image = VersatileImageField(
        'Profile Image',
        upload_to='users/profile/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    objects = ETLUserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"
