from django.shortcuts import render,HttpResponseRedirect
from . forms import INPUTFORM
from . models import info
# Create your views here.
def show(request):
    if request.method=='POST':

        form = INPUTFORM(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            roll_number = form.cleaned_data['roll_number']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            con_password = form.cleaned_data['con_password']
            texarea = form.cleaned_data['texarea']
            checkbox = form.cleaned_data['checkbox']
            payment = form.cleaned_data['payment']
            Django = form.cleaned_data['Django']
            # file = form.cleaned_data['file']
            frm = info(first_name=first_name,last_name=last_name,email=email,roll=roll_number,phone=phone_number,password=password,texarea=texarea,checkbox=checkbox,payment=payment,django=Django)
            frm.save()
            return HttpResponseRedirect('successfull')

    else:
        form = INPUTFORM()
        print('get method print')
    return render(request,'base.html',{'form':form})

def successfull(request):
    return render(request,'submit.html')