from django.forms import forms
from .models import Comment



class Newcomments(forms.Form):
    class Meta:
        model=Comment
        fields = '__all__'