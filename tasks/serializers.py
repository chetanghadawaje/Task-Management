from rest_framework import serializers
from tasks.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'created_at', 'updated_at']