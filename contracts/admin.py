from django.contrib import admin

from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('sed_number', 'reg_date', 'system', 'contractor', 'title')
    list_display_links = ('title', )
    list_per_page = 50
    list_editable = ('sed_number', 'reg_date', 'system', 'contractor')
    ordering = ('-reg_date', 'sed_number')
    search_fields = ('sed_number', 'title')
    list_filter = ('system', 'contractor')
    preserve_filters = False
    date_hierarchy = 'reg_date'

    fields = ('sed_number', 'reg_date', 'start_date', 'end_date', 'cost', 'nds',  'contractor', 'system', 'title', 'link_sed')


# admin.site.register(iSystem, iSystemAdmin)

# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     pass
