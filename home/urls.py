from django.urls import path
from . import views




app_name= 'home'

urlpatterns = [
    path('',views.home,name='home'),

    ### Users ###
    path('users_create',views.create_user,name='users_create'),

    #### Doctors Urls ####
    path('doctors_list',views.doctorls_list,name='doctors_list'),
    path('/doctors_detal/<int:pk>',views.DoctorsDetailsView.as_view(),name='doctors_detal'),
    
]