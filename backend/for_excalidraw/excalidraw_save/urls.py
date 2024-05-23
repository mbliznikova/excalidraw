from django.urls import path

from . import views

urlpatterns = [
    path("list_workspaces", views.list_workspaces, name="list_workspaces"),
    path("workspaces", views.get_workspaces, name="get_workspaces"),
    path("workspaces/<str:workspace_id>", views.save_workspace, name="save_workspace"),
    path("other", views.other, name="save_workspace"),
]
