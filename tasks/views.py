from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from tasks.models import Task
from tasks.serializers import TaskSerializers


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)