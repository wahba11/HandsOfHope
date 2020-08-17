from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctors(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    rate = models.CharField(max_length=20,null=True,blank=True)
    degree = models.CharField(max_length=20,null=True,blank=True)
    worked_before = models.TextField(null=True,blank=True)
    worked_now = models.CharField(max_length=250)
    note = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.username


class Clinic(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250,null=True,blank=True)
    landline = models.CharField(max_length=20,null=True,blank=True)
    contact_person = models.CharField(max_length=100,null=True,blank=True)
    contact_mobile = models.CharField(max_length=20,null=True,blank=True)
    contract_period = models.DateField()
    contract_start_date = models.DateField(auto_now_add=True)
    money_have_to_get = models.IntegerField(blank=True,null=True)
    doctor_assigned = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name








