from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from .models import Schedule, Step

#class ScheduleList(ListView):
#    model = Schedule
#    context_object_name = 'schedules'

class ScheduleList(ListView):
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super(ScheduleList, self).get_context_data(**kwargs)
        context['schedules'] = Schedule.objects.all()
        context['schedules_list'] = Schedule.objects.all()
        #assert False

        return context

   #context_object_name = 'schedules'


class ScheduleInfo(DetailView):
    model = Schedule
    context_object_name = 'schedule'

class StepsList(ListView):
    model = Step
    def get_context_data(self, **kwargs):
        context = super(StepsList, self).get_context_data(**kwargs)
        context['steps'] = Step.objects.all()
        return context

