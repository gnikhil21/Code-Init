from django.shortcuts import render, redirect
from .forms import register_form, login_form
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    p_form = register_form()
    if request.method == 'POST':
        p_form = register_form(request.POST)
        if p_form.data['password'] != p_form.data['c_password']:
            print('password mismatch********\n***********\n*******')
            return redirect('/accounts/register/')
        if p_form.is_valid():
            user=p_form.save()
            user.set_password(p_form.cleaned_data['password'])
            user.save()
            return redirect("/complaint/")
    content = {'personform' :p_form}
    return render(request, "register.html", content)

def login_user(request):
    form= login_form()
    if request.method == 'POST':
        form = login_form(request.POST)
        username = form.data['username']
        password = form.data['password']
        
        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
        else:
            return redirect('/accounts/login/')
        
        return redirect('/complaint/')

    content= {'form': form}
    return render(request, "login.html", content)

def logout_user(request):
    auth.logout(request)
    return redirect('/complaint/')