from django.shortcuts import render, redirect
from .models import Input
from .forms import InputForm

def index(request):
    inputs = Input.objects.all()

    context = {'inputs': inputs}

    return render(request, 'inputs/index.html', context)

def add(request):
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = InputForm()

    context = {'form' : form}


    return render(request,'inputs/add.html', context)

