# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Plan

class PlanList(ListView):
    model = Plan
    context_object_name = 'plans'

class PlanInfo(DetailView):
    model = Plan
    context_object_name = 'plan'
