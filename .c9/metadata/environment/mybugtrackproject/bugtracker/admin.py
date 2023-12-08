{"filter":false,"title":"admin.py","tooltip":"/mybugtrackproject/bugtracker/admin.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"e912e3d648bc3dff3199ca6acff920bf98de8bff","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":4,"column":50},"end":{"row":4,"column":63},"action":"remove","lines":["'reported_by'"],"id":15},{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"remove","lines":[" "]},{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"remove","lines":[","]}],[{"start":{"row":0,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["from django.contrib import admin","from .models import Bug, Project, Status","","class BugAdmin(admin.ModelAdmin):","    list_display = ['title', 'status', 'project']","    ","    # Other configurations...","","admin.site.register(Bug)","admin.site.register(Project)","admin.site.register(Status)","","'''from django.contrib import admin","from .models import Bug, Project, Status","","admin.site.register(Bug)","admin.site.register(Project)","admin.site.register(Status)'''",""],"id":16},{"start":{"row":0,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["from django.contrib import admin","from .models import Bug, Project, Status","from .forms import BugUpdateForm  # Import BugUpdateForm if you have a specific form for Bug","","class BugAdmin(admin.ModelAdmin):","    list_display = ['title', 'status', 'project', 'reported_by', 'created_at', 'updated_at', 'priority']","    form = BugUpdateForm  # Use this only if you have a specific form for Bug","    list_filter = ['status', 'project', 'reported_by', 'priority']","    search_fields = ['title', 'description', 'project']","","# Register your models here.","admin.site.register(Bug, BugAdmin)","admin.site.register(Project)","admin.site.register(Status)","","# Optional: If you had any other models previously registered (like Crop), you can unregister them","# admin.site.unregister(Crop)",""]}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["from django.contrib import admin","from .models import Bug, Project, Status","from .forms import BugUpdateForm  # Import BugUpdateForm if you have a specific form for Bug","","class BugAdmin(admin.ModelAdmin):","    list_display = ['title', 'status', 'project', 'reported_by', 'created_at', 'updated_at', 'priority']","    form = BugUpdateForm  # Use this only if you have a specific form for Bug","    list_filter = ['status', 'project', 'reported_by', 'priority']","    search_fields = ['title', 'description', 'project']","","# Register your models here.","admin.site.register(Bug, BugAdmin)","admin.site.register(Project)","admin.site.register(Status)","","# Optional: If you had any other models previously registered (like Crop), you can unregister them","# admin.site.unregister(Crop)",""],"id":17},{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["from django.contrib import admin","from .models import Bug","# Import other models if you have them, like Project and Status","","class BugAdmin(admin.ModelAdmin):","    list_display = ('title', 'reported_by', 'status', 'project', 'created_at', 'updated_at', 'priority')","    list_filter = ('status', 'project', 'priority', 'reported_by')","    search_fields = ('title', 'description', 'project')","    readonly_fields = ('created_at', 'updated_at')","","    # If you have a specific form for Bug, import and use it here","    # form = BugUpdateForm","","# Register your models here.","admin.site.register(Bug, BugAdmin)","# Register other models if needed, e.g., admin.site.register(Project)",""]}]]},"timestamp":1701896089244}