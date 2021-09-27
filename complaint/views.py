from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import updateForm, ComplaintForm
from .models import  Complaint

# Create your views here.


def index(request):
    user = request.user
    complaints = Complaint.objects.none()
    if user.is_authenticated:
        if user.is_superuser:            
            complaints = Complaint.objects.all()

            content = {
                'user': user,
                'complaints':complaints,
            }
            return render(request, 'list.html', content)

        else:
            complaints = Complaint.objects.filter(author__id=user.id)
    else:
        return redirect('/accounts/login/')
    c_form = ComplaintForm()

    if request.method == 'POST':
        if user.is_authenticated:
            c_form = ComplaintForm(request.POST)

            if c_form.is_valid():
                user_task = c_form.save()
                user_task.author = user
                user_task.save()
            return redirect('/complaint/')

    content = {
        'user': user,
        'complaints':complaints, 'c_form': c_form,
    }
    return render(request, 'list.html', content)


def delete(request, id):
    complaint = Complaint.objects.get(id=id)
    if complaint and (request.user.is_superuser):
        complaint.delete()
    return redirect('/complaint/')


def update(request, id):
    complaint = Complaint.objects.get(id=id)
    form = updateForm(instance=complaint)
    if request.method == 'POST':
        form = updateForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
        return redirect('/complaint/')
    
    content = {'complaint': complaint, 'form': form}
    return render(request, 'update.html', content)
