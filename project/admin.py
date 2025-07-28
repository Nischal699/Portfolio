from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','description','created_at','updated_at', 'file')
    
admin.site.register(Project,ProjectAdmin)

# Register your models here.
