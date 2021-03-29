from rest_framework import serializers

from .models import Trainings


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainings
        fields = ['id', 'training_name', 'from_date', 'certificate']
