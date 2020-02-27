from django.db import models

# Create your models here.
from git_auto_deploy.base_model import AppBaseModel, CHAR_FIELD_MAX_LENGTH


class Project(AppBaseModel):
    class ProjectType(models.IntegerChoices):
        django = 1, 'Django'
        react = 2, 'React'

    project_id = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    git_url = models.URLField(max_length=CHAR_FIELD_MAX_LENGTH, verbose_name='GitLab URL')
    branch = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='develop')
    os_dir = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, verbose_name='Project Directory',
                              help_text='Ex. /home/cm-django/')
    project_type = models.IntegerField(choices=ProjectType.choices)
    app_names = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, blank=True,
                                 help_text='Django app names separated by a space.')


class Log(AppBaseModel):
    text = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, null=True, blank=True)
