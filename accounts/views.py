from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('account created, login to continue'))
            return redirect('login')
    else:
        register_form = RegisterForm()
        return render(request, 'register.htm', {'register_form':register_form})


