from django.shortcuts import render,HttpResponseRedirect
from . forms import usercform
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
#create views for usercreation
def userauth(request):
    if request.method=='POST':
        frm = usercform(request.POST) # from forms.py
        if frm.is_valid():
            frm.save()

    else:
        frm=usercform()
    return render (request,'session/reg.html',{'form':frm})


#create views for login
def login_form(request):
    if request.method=='POST':
        frm = AuthenticationForm(request=request, data=request.POST) # django builtin so import AuthenticationForm
        if frm.is_valid():
            username = frm.cleaned_data['username']
            upassword = frm.cleaned_data['password']
            user = authenticate(username=username,password=upassword) #django builtin so import authenticate
            if user is not None:
                login(request,user)
            return HttpResponseRedirect('/user/success/')
    else:
        frm = AuthenticationForm()
    return render(request,'session/login.html',{'form':frm})

#create views for show login success message
def loginsuccess(request):
    return render(request,'session/success.html')


#create views for logout form
def logout_form(request):
    logout(request) # django builtin so import logout
    return HttpResponseRedirect('/user/login/')


#create views for change password
def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            frm = PasswordChangeForm(user=request.user, data=request.POST)#django builtin so import PasswordChangeForm
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)#django builtin so import update_session_auth_hash
                return HttpResponseRedirect('/user/success/')
            
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request,'session/passc.html',{'form':frm})
    else:
        return HttpResponseRedirect('/user/login/')
    
    
#create views for change password without old password
def change_pass_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            frm = SetPasswordForm(user=request.user, data=request.POST)#django builtin so import SetPasswordForm
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)#django builtin so import update_session_auth_hash
                return HttpResponseRedirect('/user/success/')
            
        else:
            frm = SetPasswordForm(user=request.user)
        return render(request,'session/without_old_pass.html',{'form':frm})
    else:
        return HttpResponseRedirect('/user/login/')
    
    


