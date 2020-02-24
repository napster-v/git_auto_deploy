# Create your views here.
import os
import subprocess

from rest_framework import generics, status
from rest_framework.response import Response

from auto_deploy.models import Project
from auto_deploy.serializers import ProjectLogSerializer


class ProjectLog(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectLogSerializer

    def create(self, request, *args, **kwargs):
        serializer: ProjectLogSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        project_id = data['project']['id']
        project = Project.objects.get(project_id=project_id)
        print(os.getcwd())
        os.chdir(project.os_dir)
        print(os.getcwd())
        subprocess.run('git commit -m "first commit"', shell=True)
        subprocess.run('git push -u origin master', shell=True)
        return Response(status=status.HTTP_200_OK)
