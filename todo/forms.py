from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields =['title']
        labels ={'title': 'My Todo'}

class TodoUpdate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','completed']
        labels = {'title':'My Todo'}
        
        