"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import (
    registration_view,
    logout_view,
    login_view,
    must_authenticate_view,
)
from todo.views import(
    home_view,
    create_task_view,
    edit_task_view,

)
app_name = 'todo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name= 'home'),
    path('task-create/',create_task_view,name='task'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('must_authenticate/', must_authenticate_view, name='must_authenticate'),
    path('<slug>/task-update/', edit_task_view, name='update'),

]
