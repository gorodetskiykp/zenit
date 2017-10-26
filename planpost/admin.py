from django.contrib import admin

from .models import Plan

@admin.register(Plan)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('year', )
    list_display_links = ('year', )
    list_per_page = 50
    # list_editable = ('sed_number', 'reg_date', 'system', 'contractor')
    ordering = ('-year', )
    # search_fields = ('fio', )
    list_filter = ('year', )
    preserve_filters = False
    # date_hierarchy = 'reg_date'
    # inlines = (EmailsInline, PhonesInline, Organization_Based_RoleInline)
