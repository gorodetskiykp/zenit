import django_tables2 as tables
from django_tables2.utils import A
from .models import Contract

class ContractTable(tables.Table):
    sed_number = tables.LinkColumn('contracts:detail', text=lambda record: record.sed_number, args=[A('pk')])
    # group = tables.LinkColumn('grps:detail', text=lambda record: record.group, args=[A('group.pk')])
    class Meta:
        model = Contract
        attrs = {'class': 'table table-bordered'}
        fields = ['sed_number', 'reg_date', 'contractor', 'title', 'system']
