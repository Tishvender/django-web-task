from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EmployeeForm,SignupForm
from .models import Employee
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
#Employee Data
def employeeview(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
           nm= fm.cleaned_data['name']
           ct = fm.cleaned_data['contact']
           em = fm.cleaned_data['email_department']
           reg = Employee(name= nm, contact = ct ,email_department = em)
           reg.save()
           fm = EmployeeForm()
    else:
        fm = EmployeeForm()
    emp = Employee.objects.all()
    return render(request, 'app/employeeview.html', {'form':fm, 'em':emp})
#Signup
def signup(request):
    if request.method == 'POST':
        sf = SignupForm(request.POST)
        if sf.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            sf.save()
    else:
        sf = SignupForm()
    return render(request, 'app/signup.html', {'signupform':sf})
#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'app/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'app/profile.html', {'name' : request.user})
    else:
        return HttpResponseRedirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')