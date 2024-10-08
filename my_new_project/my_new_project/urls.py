"""
URL configuration for my_new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tasks/new/", views.TaskCreateView.as_view(), name="task-create"),
    re_path(
        r"^tasks/(?P<id>\d+)/$", views.TaskDetailView.as_view(), name="task-detail"
    ),
    re_path(
        r"^tasks/(?P<id>\d+)/edit/$", views.TaskUpdateView.as_view(), name="task-edit"
    ),
    re_path(
        r"^tasks/(?P<id>\d+)/delete/$",
        views.TaskDeleteView.as_view(),
        name="task-delete",
    ),
]
