from django import forms
from django.forms import ModelForm

from .models import Tasks


class AddTaskForm(forms.ModelForm):

    task = forms.CharField(max_length=200,
                            widget = forms.TextInput(
                                attrs= {
                                    'class': 'form-control',
                                    'placeholder': 'tasks?',
                                }
                            )
                            )

    class Meta:
        model = Tasks
        fields = '__all__'