from django.urls import path

from auto_deploy.views import ProjectLog

urlpatterns = [
    path('deploy/', ProjectLog.as_view())
]
