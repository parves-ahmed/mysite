from rest_framework import serializers

from .models import Trainings, ProjectType, Projects


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainings
        fields = ['id', 'training_name', 'from_date', 'certificate']


class GetProjectByProjectTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'project_name', 'company']
