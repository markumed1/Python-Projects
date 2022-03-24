from random import choices

from django.db import models


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.')
]

class Person(models.Model):
    Title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.CharField(max_length=60)
    Username = models.CharField(max_length=60)

    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.person = None

    def __str__(self):
        return self.person

