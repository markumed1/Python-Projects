# import models top of page before creating class
from django.db import models


# write your models
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(default=0.0)

    #   is the default model manager and each model needs to have at least ONE model manager
    objects = models.Manager()

    def __str__(self):
        return self.title
