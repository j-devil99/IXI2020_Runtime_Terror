from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from multiselectfield import MultiSelectField
from .choices import QUALIFICATION_CHOICES, GENDER_CHOICES, CATEGORY_CHOICES, DOMAIN_CHOICES

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    GPA = models.FloatField(max_length=10.0, default=0.0)
    dob = models.DateField(null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    gender = MultiSelectField(choices=GENDER_CHOICES, null=True)
    category = MultiSelectField(choices=CATEGORY_CHOICES, null=True)
    qualification = MultiSelectField(choices=QUALIFICATION_CHOICES, null=True)
    domain = MultiSelectField(choices=DOMAIN_CHOICES, null=True)