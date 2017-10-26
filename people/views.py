from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_tables2 import RequestConfig

from .models import People

class PeopleList(ListView):
    model = People
    context_object_name = 'people'

class PeopleInfo(DetailView):
    model = People
    context_object_name = 'people'
