from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.training_list, name='training_list')
]