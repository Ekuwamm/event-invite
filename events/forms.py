from django import forms 
from .import models

class CreateEvent(forms.ModelForm):
    class Meta:
        model = models.myevent
        fields = ['title','body1','body1','body2','body3','body4','slug','banner']