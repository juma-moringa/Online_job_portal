from django.contrib.auth.forms import UserCreationForm
from .models import Employer, User,Client
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