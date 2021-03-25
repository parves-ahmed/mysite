from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TrainingForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        form = TrainingForm()
        return render(request, 'my_app/training_form.html', {'form': form})
    else:
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/list')


def training_list(request):
    return HttpResponse("ok")
