from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login , logout 
from django.contrib.auth.decorators import login_required

def sign_up(request):
    fm=None
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully !!')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'sign_up.html',{'form':fm})
# without authentication
# def user_login(request):
#     if request.method == "POST":
#         fm=AuthenticationForm(request=request,data=request.POST)
#         if fm.is_valid():
#             uname=fm.cleaned_data['username']
#             upass=fm.cleaned_data['password']
#             user=authenticate(username=uname,password=upass)
#             if user is not None:
#                 login(request,user) 
#                 messages.success(request,"Logged in Successfully!!")
#                 return HttpResponseRedirect("UserProfile")
#     else:
#         fm=AuthenticationForm()
#     return render(request,'userlogin.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user) 
                    messages.success(request,"Logged in Successfully!!")
                    return HttpResponseRedirect("UserProfile")
        else:
            fm=AuthenticationForm()
        return render(request,'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('UserProfile')

@login_required
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('userlogin')
# request.user provides access to the user data associated with the currently authenticated user's session, and you can use it to retrieve user-specific information, including their name.

# @login_required
# def user_profile(request):
#     if request.user.is_authenticated:
#         return HttpResponse("you can access this site")
#     else:
#         return HttpResponse("you cannot access this site")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect ('userlogin')