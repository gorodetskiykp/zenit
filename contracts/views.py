from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_tables2 import RequestConfig

from .models import Contract
from .tables import ContractTable

class ContractList(ListView):
    model = Contract
    context_object_name = 'contracts'

def contract_list(request):
    table = ContractTable(Contract.objects.all())
    RequestConfig(request, paginate={'per_page': 50}).configure(table)
    return render(request, 'contracts/contracts_table.html', {'table': table})


class ContractInfo(DetailView):
    model = Contract
    context_object_name = 'contract'
