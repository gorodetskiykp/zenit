from django.shortcuts import render
from django.views.generic import ListView as LV


from .models import WhatsNew

class WhatsNewList(LV):
    model = WhatsNew
    context_object_name = 'releases'
