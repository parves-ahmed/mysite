from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload_cover_imaage/', views.CoverImageView.as_view()),
    path('trainings/', views.training, name='training'),
    path('list', views.training_list, name='training_list'),
    path('api/trainings/', views.TrainingList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)