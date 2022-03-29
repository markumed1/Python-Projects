from django.forms import ModelForm
from .models import Person

class ContactForm(ModelForm):
    class Meta:
        model = Person
        field = '__all__'