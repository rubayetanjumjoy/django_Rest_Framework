from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from djangorestapp import models
from django.contrib.auth.models import User

class article(forms.ModelForm):
    class Meta:
        model = models.Article
        fields= "__all__"

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields= "__all__"
