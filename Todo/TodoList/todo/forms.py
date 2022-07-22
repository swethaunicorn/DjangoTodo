from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','complete']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','complete']

    def save(self, commit=True):
        task_post = self.instance
        task_post.title = self.cleaned_data['title']
        task_post.description = self.cleaned_data['description']
        task_post.complete = self.cleaned_data['complete']

        if commit:
            task_post.save()
        return task_post