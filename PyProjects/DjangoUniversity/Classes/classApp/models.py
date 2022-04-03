# import models top of page before creating class
from datetime import timedelta

from django.db import models


# write your models
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(blank=True, null=True)
    instructor_name = models.CharField(max_length=60)
    duration = models.DurationField(default=timedelta())

    #   is the default model manager and each model needs to have at least ONE model manager
    objects = models.Manager()

    def __str__(self):
        return self.title

