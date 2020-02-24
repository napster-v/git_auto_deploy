from django.urls import path

from auto_deploy.views import ProjectLog

urlpatterns = [
    path('test/', ProjectLog.as_view())
]
