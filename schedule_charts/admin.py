from django.contrib import admin

#from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Schedule, Step

#@admin.register(Step)
#class StepAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Step, MPTTModelAdmin)

admin.site.register(
    Step,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'date_begin',
        'date_end',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

class StepInline(admin.TabularInline):
    model = Step
    extra = 1

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'system', 'contract')
    list_display_links = ('title', )
    list_per_page = 50
    # list_editable = ('sed_number', 'reg_date', 'system', 'contractor')
    ordering = ('system', )
    search_fields = ('title', )
    list_filter = ('system', )
    preserve_filters = False
    
    inlines = (StepInline, )
    # date_hierarchy = 'reg_date'

    # fields = (('sed_number', 'reg_date'), ('ext_number', 'sed_project_number'), 'contractor', 'system', 'title', 'link_sed')


# admin.site.register(iSystem, iSystemAdmin)

# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     pass

# Register your models here.
