from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    # CHOICES = [('Developer','Developrer'),('Employee','Employee')]
    # Choices=forms.CharField(label='Work As ..', widget=forms.RadioSelect(choices=CHOICES))
    name=models.CharField(null=True,max_length=200)
    age=models.IntegerField(null=True)
    Experience=models.CharField(null=True,max_length=200)
    country=models.CharField(null=True,max_length=200)
    location=models.CharField(null=True,max_length=200)
    Email=models.CharField(null=True,max_length=200)
    Phone=models.CharField(null=True,max_length=200)
    Internship=models.CharField(null=True,max_length=200)
    Bio=models.CharField(null=True,max_length=1000)
    skill_1=models.CharField(null=True,max_length=200)
    skill_2=models.CharField(null=True,max_length=200)
    skill_3=models.CharField(null=True,max_length=200)
    profile_pics=models.ImageField(default="unknown.png",null=True,blank=True)
    # def __str__(self):
    #     return self.user.username
    

