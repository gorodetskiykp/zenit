from django.contrib import admin
from django.db import models

from .models import Document_Type, Document

# class StatusInline(admin.TabularInline):
#     model = Status
#     extra = 1

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_type', 'doc_date', 'creator', )
    list_filter = ('doc_type', )
    ordering = ('doc_name', )
    # inlines = (StatusInline, )


@admin.register(Document_Type)
class Document_TypeAdmin(admin.ModelAdmin):
    # list_display = ('doc_name', 'doc_type', 'doc_date', 'creator', )
    # list_filter = ('doc_type', )
    ordering = ('doc_type', )