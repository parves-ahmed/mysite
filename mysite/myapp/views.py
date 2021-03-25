from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import TrainingForm

# Create your views here.
from .models import Trainings
from .serializers import TrainingSerializer


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


class TrainingList(APIView):
    def get(self, request, format=None):
        trainings = Trainings.objects.all()
        serializer = TrainingSerializer(trainings, many=True)
        return Response(serializer.data)
