from django.contrib import admin
from .models import Bug
# Import other models if you have them, like Project and Status

class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'reported_by', 'status', 'project', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'project', 'priority', 'reported_by')
    search_fields = ('title', 'description', 'project')
    readonly_fields = ('created_at', 'updated_at')

    # If you have a specific form for Bug, import and use it here
    # form = BugUpdateForm

# Register your models here.
admin.site.register(Bug, BugAdmin)
# Register other models if needed, e.g., admin.site.register(Project)
