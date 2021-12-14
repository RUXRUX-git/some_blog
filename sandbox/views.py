from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from sandbox.forms import UserForm


# Create your views here.

def message_list(request):
    return render(request, 'sandbox/base.html', {})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('create_user')
    else:
        form = UserForm()

    return render(request, 'sandbox/create_user.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        raise NotImplementedError
    else:
        return render(request, 'sandbox/log_in.html', {})
