import django_tables2 as tables
from .models import iSystem
import itertools
from django.utils.html import format_html


class Report7117Table(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='№', orderable=False)
    administrators = tables.Column(verbose_name=format_html('Администраторы<br />- Основной<br />- Резервный<br />- Бюджет<br />- Доступы'), orderable=False)
    all_names = tables.TemplateColumn('''
    {% if request.user.is_superuser %}
    <a href="/admin/isystems/isystem/{{ record.id }}/change/" target="_blank">{{ value }}</a>
    {% else %}{{ value }}{% endif %}
    ''', verbose_name='Краткое название (Полное название)', order_by=('short_name',))
    project = tables.Column(empty_values=())
    system_type = tables.Column('Тип ИС', empty_values=())
    system_function = tables.Column('Назначение ИС', empty_values=())
    dates = tables.Column(empty_values=(), accessor='statuses.all', verbose_name='Ключевые даты', orderable=False)
    info_categories = tables.Column(empty_values=(), verbose_name='Категории обрабатываемой информации', orderable=False)
    functional_customers = tables.Column(empty_values=(), verbose_name='Функциональные заказчики', orderable=False)
    maintenance = tables.Column()
    #
    def __init__(self, *args, **kwargs):
        super(Report7117Table, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
    #
    def render_row_number(self):
        return format_html('{}'.format(next(self.counter) + 1))
    #
    def render_administrators(self, value):
        return format_html('{}'.format('<br />'.join(value.split(';'))))
    #
    def render_system_function(self, value):
        if value == None:
            return ''
        else:
            return value
    #
    def render_project(self, value):
        if value == None:
            return ''
        else:
            return value
    #
    def render_dates(self, value):
        statuses = []
        statuses_dict = {}
        for status in value:
            formatted_status_date = status.status_date.strftime('%d.%m.%Y') if status.status_date else ''
            status_title = status.status
            if status.link_eatd:
                status_title = '<a href="{}" target="_blank">{}</a>'.format(status.link_eatd, status.status)
            statuses_dict[status.status_date] = '{} - {}'.format(formatted_status_date, status_title)
        for status_date in sorted(statuses_dict.keys()):
            statuses.append(statuses_dict[status_date])
        return format_html('<br />'.join(statuses))
    #
    def render_info_categories(self, value):
        return format_html(value)

    def render_functional_customers(self, value):
        return format_html(value)

    class Meta:
        model = iSystem
        attrs = {'class': 'table table-striped table-bordered table-hover table-condensed small'}
        row_attrs = {
            'class': lambda record: 'danger' if record.critical else ''
        }
        fields = (
            'row_number', 'all_names', 'administrators', 'project', 'system_type', 'system_function',
            'dates', 'info_categories', 'functional_customers')


class ReportShortsTable(tables.Table):
    full_name = tables.Column('Полное наименование ИС', empty_values=())
    short_name = tables.Column('Краткое наименование ИС', empty_values=())
    abbreviation = tables.Column('Краткое наименование ИС - латиница', empty_values=())


    class Meta:
        model = iSystem
        attrs = {'class': 'table table-striped table-bordered table-hover table-condensed small'}
        fields = ('full_name', 'short_name')
