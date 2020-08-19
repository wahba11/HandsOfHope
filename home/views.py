from django.shortcuts import render, redirect
from django.views.generic import (ListView,DetailView)
from django.contrib.auth.models import User
from . import models
from .forms import UserForm
from django.db.models import F


# Create your views here.

def home(request):
    doctors = models.Doctors.objects.all()
    clinics = models.Clinic.objects.all()
    context = {"doctors":doctors,"clinics":clinics}
    return render(request,'home/home.html',context)



def create_user(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            first_name = userform.cleaned_data['first_name']
            last_name = userform.cleaned_data['last_name']
            password1 = userform.cleaned_data['password1']
            password2 = userform.cleaned_data['password2']
            is_active = userform.cleaned_data['is_active']
            is_superuser = userform.cleaned_data['is_superuser']
            userform.save()

            return redirect('home:users_create')

    context = {'userform':userform}
    return render(request,'home/user_form.html',context)


# class DoctorsListView(ListView):
#     model = models.Doctors
#     # model = User
#     template_name = 'doctors_list'

def doctorls_list(request):
    doctors = models.Doctors.objects.all()
    users = User.objects.all()

    context = {'doctors_list':doctors,'users':users}

    return render(request,'home/doctors_list.html',context)

class DoctorsDetailsView(DetailView):
    model = models.Doctors

