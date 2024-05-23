from django.contrib import admin
from .models import Workspace


class WorkspaceAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    pass

admin.site.register(Workspace, WorkspaceAdmin)