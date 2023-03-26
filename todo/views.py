from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def singupuser(request):
    if request.method == 'GET':
        return render(request,'todo/singupuser.html',{'form':UserCreationForm()})
    else:
        # Create new user
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/singupuser.html',{'form':UserCreationForm(),'error':'This username has already been taken'})
        else:
            #Error pas1==pas2 
            return render(request,'todo/singupuser.html',{'form':UserCreationForm(),'error':'Password did not math'})
            
# if create new user            
def currenttodos(request):
    return render(request,'todo/currenttodos.html')
