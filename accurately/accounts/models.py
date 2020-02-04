from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from multiselectfield import MultiSelectField
from .choices import QUALIFICATION_CHOICES, GENDER_CHOICES, CATEGORY_CHOICES, DOMAIN_CHOICES

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)

class Student(models.Model):
    GPA = models.FloatField(max_length=10.0)
    dob = models.DateField()
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender = MultiSelectField(choices=GENDER_CHOICES)
    category = MultiSelectField(choices=CATEGORY_CHOICES, null=True)
    qualification = MultiSelectField(choices=QUALIFICATION_CHOICES, null=True)
    domain = MultiSelectField(choices=DOMAIN_CHOICES, null=True)