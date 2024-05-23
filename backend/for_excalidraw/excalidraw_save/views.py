import datetime
import json
import logging

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Workspace

logger = logging.getLogger(__name__)

def list_workspaces(request):
    workspaces = {
        "response": [
            w for w in Workspace.objects.order_by("save_date")
        ]
    }
    return render(request, "workspaces.html", workspaces)


def get_workspaces(request):
    workspace_response = {
        "response": [
            {
                "workspace_id": w.workspace_id,
            } for w in Workspace.objects.order_by("save_date")
        ] 
    }
    
    return JsonResponse(workspace_response)
    

@csrf_exempt
def save_workspace(request, workspace_id: str):
    try:
        workspace = Workspace.objects.get(workspace_id=workspace_id)
    except Workspace.DoesNotExist:
        workspace = None

    if request.method == 'GET':
        if workspace:
            return HttpResponse(workspace.workspace_state, content_type="application/json")
        else:
            return JsonResponse({"error": "No such workspace"}, status=404)

    elif request.method == 'POST':
        workspace_state = json.loads(request.body)
        save_date = datetime.datetime.now()

        if workspace:
            print('Update workspace')
            workspace.workspace_state = json.dumps(workspace_state)
            workspace.save_date = save_date
        else:
            print('Create workspace')
            workspace = Workspace(
                workspace_id = workspace_id,
                workspace_state = json.dumps(workspace_state),
                save_date = save_date
                )

        workspace.save()

    print('inside view')

    return JsonResponse(workspace_state)


def other(request):
    print('inside other')
    return JsonResponse({"error": None, "other": "yes"})