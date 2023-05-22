
from rest_framework import serializers
from user.models import *
from .models import Task
from user.serializers import SingleUserSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'


class TaskDisplaySerializer(serializers.ModelSerializer):
    user = SingleUserSerializer()
    class Meta:
        model = Task
        fields ='__all__'