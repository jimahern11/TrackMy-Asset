from django import forms
from trips_app.models import Trips

class TaskForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['task', 'done']   
