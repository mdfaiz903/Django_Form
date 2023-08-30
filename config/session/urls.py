
from django.urls import path
from . views import userauth,login_form,loginsuccess,logout_form,change_pass,change_pass_without_old_pass
urlpatterns = [
    path('reg/',userauth,name='reg'),#for registation
    path('login/',login_form,name='login_form'),#for login
    path('success/',loginsuccess,name='loginsuccess'),#for show success message
    path('logout/',logout_form,name='logout_form'),#for logout form
    path('passc/',change_pass,name='change_pass'),#for password change
    path('without_old_passc/',change_pass_without_old_pass,name='without_old_passc'),#for password change without old pass
]
