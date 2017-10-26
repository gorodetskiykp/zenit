from django.contrib import admin

from .models import WhatsNew

@admin.register(WhatsNew)
class WhatsNewAdmin(admin.ModelAdmin):
    pass
