from django.contrib import admin
from .models import People, Organization_Based_Role, Emails, Phone, Phone_Type, System_Based_Role

class EmailsInline(admin.TabularInline):
    model = Emails
    extra = 0

class PhonesInline(admin.TabularInline):
    model = Phone
    extra = 0

class Organization_Based_RoleInline(admin.TabularInline):
    model = Organization_Based_Role
    extra = 0
    fields = ('post', 'organization')

class System_Based_RoleInline(admin.TabularInline):
    model = System_Based_Role
    extra = 0
    fields = ('role', 'system')

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('fio', )
    list_display_links = ('fio', )
    list_per_page = 50
    # list_editable = ('sed_number', 'reg_date', 'system', 'contractor')
    ordering = ('fio', )
    search_fields = ('fio', )
    # list_filter = ('system', 'contractor')
    # preserve_filters = False
    # date_hierarchy = 'reg_date'
    inlines = (EmailsInline, PhonesInline, Organization_Based_RoleInline)#, System_Based_RoleInline)

@admin.register(System_Based_Role)
class System_Based_RoleAdmin(admin.ModelAdmin):
    list_display = ('people', 'system', 'role')
    list_display_links = ('people', )
    list_per_page = 50
    # list_editable = ('sed_number', 'reg_date', 'system', 'contractor')
    ordering = ('people', )
    search_fields = ('people', )
    # list_filter = ('system', 'contractor')
    # preserve_filters = False
    # date_hierarchy = 'reg_date'
    # inlines = (Organization_Based_RoleInline, )

@admin.register(Phone_Type)
class Phone_TypeAdmin(admin.ModelAdmin):
     pass

# @admin.register(Organization_Based_Role)
# class Organization_Based_RoleAdmin(admin.ModelAdmin):
#     pass
