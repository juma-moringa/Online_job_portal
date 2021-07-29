from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Candidates, Company, Employer, User,Client
from django.db import transaction
from django import forms 


class ClientRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','phone_number','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.save()
        return user

class EmployerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ['username','email','phone_number','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        employer.save()
        return user  


class JobApplicationForm(ModelForm):
    class Meta:
        model = Candidates
        fields = ['name','birth_date','gender','phone_number','email','resume','company']       

class AddjobForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name','position','description','salary','experience','Location']  


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')   