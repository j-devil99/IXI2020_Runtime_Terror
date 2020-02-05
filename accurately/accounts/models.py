from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from multiselectfield import MultiSelectField
from .choices import QUALIFICATION_CHOICES, GENDER_CHOICES, CATEGORY_CHOICES, DOMAIN_CHOICES

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False, default='john@doe.com')
    GPA = models.FloatField(max_length=10.0, default=8.0)
    country = models.CharField(max_length=20, null=True)
    category = MultiSelectField(choices=CATEGORY_CHOICES, null=True)
    qualification = MultiSelectField(choices=QUALIFICATION_CHOICES, null=True)
    domain = MultiSelectField(choices=DOMAIN_CHOICES, null=True)

class Opp(models.Model):
    index = models.IntegerField(null=True)
    Id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=4000)
    about = models.CharField(max_length=10000, null=True)
    date = models.CharField(max_length=10000,null=True)
    link = models.URLField(max_length=10000,null=True)
    link2 = models.URLField(max_length=10000,null=True)
    cataegories =  models.CharField(max_length=10000, null=True)
    domain = models.CharField(max_length=10000,null=True)
    education = models.CharField(max_length=10000,null=True)
    country = models.CharField(max_length=2000, null=True)
    