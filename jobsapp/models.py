from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone_number = models.IntegerField(default=0,null=False)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user.username

    #company model class
class Company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    Location = models.CharField(max_length=100, null=True)
    

    def __str__ (self):
        return self.name

    @classmethod
    def search_by_position(cls,search_term):
    	jobs = cls.objects.filter(position__icontains=search_term)
    	return jobs
  


    #candidates model class
class Candidates(models.Model):
    gender_selection = (('Male', 'male'),('Female', 'female'),('Prefer not to say','prefer not to say'))
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=60, null=True)
    phone_number = models.IntegerField(default=0, null=True)
    birth_date = models.DateField(null=True)
    company = models.ManyToManyField(Company, blank=True)
    gender = models.CharField(choices=gender_selection, max_length=50, null=True )
    resume = models.FileField(null=True)
    

    def __str__ (self):
        return self.name

