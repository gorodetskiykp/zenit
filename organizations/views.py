from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import OrganizationForm
from .models import Organization


class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organizations'


class OrganizationInfo(DetailView):
    model = Organization
    context_object_name = 'organization'
    
    
def save_organization_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            organizations = Organization.objects.all()
            data['html_organization_list'] = render_to_string('organizations/table.html', {
                'organizations': organizations
            }, request=request)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
    else:
        form = OrganizationForm()
    return save_organization_form(request, form, 'organizations/organization_create.html')
    

def organization_update(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
    else:
        form = OrganizationForm(instance=organization)
    return save_organization_form(request, form, 'organizations/organization_update.html')
    

