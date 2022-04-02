from django.db import models

TITLE_CHOICES = {
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
}


class DjangoClasses(models.Model):
    title = models.CharField(max_length=5)
    course_number = models.CharField(max_length=10)
    instructor_name = models.CharField(max_length=30)
    duration = models.CharField(max_length=10)

    objects = models.Manager()

    def __str__(self):
        return self.title

