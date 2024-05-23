from django.db import models

class Workspace(models.Model):
    def __str__(self) -> str:
        return f'Workspace {self.workspace_id}'

    workspace_id = models.CharField(max_length=20)
    save_date = models.DateTimeField("saved at")
    workspace_state = models.TextField()
