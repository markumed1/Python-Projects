from django.db import models

TITLE_CHOICES = {
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
}


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    course_number = models.CharField(max_length=20)
    instructor_name = models.CharField(max_length=60)
    duration = models.CharField(max_length=20)




    objects = models.Manager

    def __str__(self):
        return self.instructor_name