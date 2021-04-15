from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import TrainingForm, UploadCoverImage

# Create your views here.
from .models import Trainings, CoverImage, Projects, ProjectType, Companies
from .serializers import TrainingSerializer


# index page
def index(request):
    cover_image_list = CoverImage.objects.all()
    # print(cover_image_list[0].photos.url)

    final_dict = {}
    all_company = Companies.objects.distinct()
    for cm in all_company:
        all_projects = Projects.objects.filter(company_id=cm)
        all_project_type = [e.project_type for e in all_projects]
        final_dict[cm] = pp_type(all_project_type)

    # print(all_projects[0].project_name if all_projects else '')
    # print([e.company for e in all_projects])
    # print(final_dict)
    return render(request, 'my_app/index.html', {'cover_photos': cover_image_list, 'projects': final_dict})


def pp_type(all_project_type):
    project_ptype_dict = {}
    for pt in all_project_type:
        project_ptype_dict[pt] = Projects.objects.filter(project_type_id=pt)
    return project_ptype_dict


# upload cover image
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


class Project(View):
    def get(self, request, *args, **kwargs):
        all_projects = Projects.objects.all()
        return render(request, 'my_app/index.html', {'projects': all_projects})


# Manage training in functional way
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


# Manage training through API
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
