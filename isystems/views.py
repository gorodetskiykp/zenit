# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import iSystem
import csv
from django.http import HttpResponse
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from .tables import Report7117Table, ReportShortsTable

# from django_filters.views import FilterView
import django_filters


class SystemList(ListView):
    model = iSystem
    context_object_name = 'systems'


class SystemInfo(DetailView):
    model = iSystem
    context_object_name = 'system'
    

class ISReport7117(ExportMixin, SingleTableView):
    model = iSystem
    table_class = Report7117Table
    template_name = 'isystems/is_report_7117.html'

    # filterset_class = ISReport7117Filter

    table_pagination = {
        'per_page': 100
    }

#
# def is_report_7117_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="71-17.csv"'
#     response.write(u'\ufeff'.encode('utf8'))
#     writer = csv.writer(response, delimiter=';', dialect='excel')
#     writer.writerow([
#         'Краткое наименвание',
#         'Полное наименование',
#         'Проект',
#         'Тип',
#         'Назначение',
#         'Ключевые даты',
#         'Категории обрабатываемой информации',
#         'Критичность для функционирования организации',
#         'Функциональные заказчики',
#         'Техническое сопровождение',
#         'Основной администратор',
#         'Резервный администратор',
#         'Куратор договора / бюджета',
#         'Администратор информационной безопасности',
#
#     ])
#     systems = iSystem.objects.order_by('short_name')
#     for system in systems:
#         statuses = []
#         statuses_dict = {}
#         for status in system.statuses.all():
#             formatted_status_date = status.status_date.strftime('%d.%m.%Y') if status.status_date else ''
#             status_title = status.status
#             # if status.link_eatd:
#             #     status_title = '<a href="{}" target="_blank">{}</a>'.format(status.link_eatd, status.status)
#             statuses_dict[status.status_date] = '{} - {}'.format(formatted_status_date, status_title)
#         for status_date in sorted(statuses_dict.keys()):
#             statuses.append(statuses_dict[status_date])
#         dates = '\n'.join(statuses)
#
#         writer.writerow([
#             system.short_name,
#             system.full_name,
#             system.project.title if system.project else '',
#             system.system_type,
#             system.system_function,
#             dates,
#             system.info_categories,
#             '+' if system.critical else '-',
#             system.functional_customers,
#             system.maintenance.short_name if system.maintenance else '',
#             system.administrator.people.short_fio if system.administrator else '',
#             system.reserve_administrator.people.short_fio if system.reserve_administrator else '',
#             system.contract_administrator.people.short_fio if system.contract_administrator else '',
#             system.isecurity_administrator.people.short_fio if system.isecurity_administrator else '',
#         ])
#
#     return response


# class ISReportShorts(SingleTableView):
class ISReportShorts(ExportMixin, SingleTableView):
    model = iSystem
    table_class = ReportShortsTable
    template_name = 'isystems/is_report_shorts.html'
    table_pagination = {
        'per_page': 100
    }

    def get_queryset(self):
        isystems = iSystem.objects.filter(system_type='Локальная')
        return isystems


# def is_report_shorts_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="shorts.csv"'
#     response.write(u'\ufeff'.encode('utf8'))
#     writer = csv.writer(response, delimiter=';', dialect='excel')
#     writer.writerow([
#         'Полное наименование ИС',
#         'Краткое наименование ИС',
#         'Краткое наименование ИС - латиница',
#         'код организации',
#     ])
#     systems = iSystem.objects.filter(system_type='Локальная').order_by('short_name')
#     for system in systems:
#         writer.writerow([
#             system.short_name,
#             system.full_name,
#             system.abbreviation,
#             'DN',
#         ])
#
#     return response