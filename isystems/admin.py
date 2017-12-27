from django.contrib import admin
from django.db import models

from .models import iSystem, Status, Project, Life_Step

class StatusInline(admin.TabularInline):
    model = Status
    extra = 1

@admin.register(iSystem)
class iSystemAdmin(admin.ModelAdmin):
    list_display = (
        'short_name', 
        'abbreviation', 
        'full_name', 
        'shadow', 
        'responsibility_center'
    )
    list_editable = ('shadow', 'responsibility_center')
    list_filter = ('system_type',)
    # list_filter = ('short_name', 'developer', )
    ordering = ('short_name',)
    inlines = (StatusInline, )

# admin.site.register(iSystem, iSystemAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    ordering = ('title', )
#    list_filter = ('staqtus', )


@admin.register(Life_Step)
class Life_StepAdmin(admin.ModelAdmin):
    list_display = ('step', 'position')
    ordering = ('position', 'step')
