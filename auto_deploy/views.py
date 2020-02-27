# Create your views here.
import os
import subprocess
import time

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
        os.chdir(project.os_dir)
        if project.project_type == 1:
            subprocess.run('git stash', shell=True)
            time.sleep(2)
            subprocess.run(f'git pull origin {project.branch} -f', shell=True)
            time.sleep(5)
            subprocess.run(f'python manage.py makemigrations {project.app_names}', shell=True)
            time.sleep(5)
            subprocess.run(f'python manage.py migrate', shell=True)
            time.sleep(5)
            subprocess.run(f'sudo service apache2 restart', shell=True)

        elif project.project_type == 2:
            subprocess.run(f'git pull origin {project.branch} -f', shell=True)
            time.sleep(5)
            subprocess.run(f'sudo service apache2 restart', shell=True)

        return Response(status=status.HTTP_200_OK)
