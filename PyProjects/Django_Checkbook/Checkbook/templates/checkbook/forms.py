from django.forms import ModelForm
from .models import Checkbook

class Checkbook:
    pass


class Checkbook(ModelForm):
    class Meta:
        model = Checkbook
        fields = '__all__'
