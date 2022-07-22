from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account as acc
from .models import Task
from .forms import CreateTaskForm,UpdateTaskForm
from django.urls import reverse_lazy


def home_view(request):
    context = {}
    return render(request, 'todo/home.html', context)

## for Admin
def create_task_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateTaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = acc.objects.filter(email= user.email).first()
        obj.author = author
        obj.save()
        form = CreateTaskForm()

    context['form'] = form
    return render(request, 'todo/create_task.html', context)

def detail_blog_view(request, slug):
    context = {}

    task_post = get_object_or_404(Task, slug=slug)
    context['task_post'] = task_post
    return render(request, 'todo/detail_task.html', context)


def edit_task_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    task_post = get_object_or_404(Task, slug=slug)
    if request.POST:
        form = UpdateTaskForm(request.POST or None, request.FILES or None, instance=task_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Updated'
            task_post = obj
    form = UpdateTaskForm(
        initial={
            "title": task_post.title,
            "description": task_post.description,
            "complete": task_post.complete
        }
    )
    context['form'] = form
    return render(request, 'todo/update_task.html', context)