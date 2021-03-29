from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import TrainingForm, UploadCoverImage

# Create your views here.
from .models import Trainings, CoverImage
from .serializers import TrainingSerializer


def index(request):
    cover_image_list = CoverImage.objects.all()
    print(cover_image_list[0].photos.url)
    return render(request, 'my_app/index.html', {'cover_photos': cover_image_list})


class CoverImageView(FormView):
    form_class = UploadCoverImage
    template_name = 'my_app/cover_image.html'
    success_url = '/list'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('photos')
        if form.is_valid():
            for f in files:
                file_instance = CoverImage(photos=f)
                file_instance.save()
            print('success')
            return self.form_valid(form)
        else:
            print('err')
            return self.form_invalid(form)


def training(request):
    if request.method == 'GET':
        form = TrainingForm()
        return render(request, 'my_app/training_form.html', {'form': form})
    else:
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def training_list(request):
    return HttpResponse("ok")


class TrainingList(APIView):
    def get(self, request, format=None):
        trainings = Trainings.objects.all()
        # print(trainings[0].training_name)
        serializer = TrainingSerializer(trainings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
