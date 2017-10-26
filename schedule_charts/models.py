from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt

class Schedule(models.Model):
    title       = models.TextField(verbose_name='Название графика', default='План-график', null=False, blank=False)
    contract    = models.ForeignKey('contracts.Contract', verbose_name='Договор', default='', blank=True, null=True, related_name='schedules')
    system      = models.ForeignKey('isystems.iSystem', verbose_name='Система', default='', blank=True, null=True, related_name='schedules')
    link        = models.URLField(verbose_name='Ссылка на скан в ЭАТД', blank=True, null=True)
    # reg_date            = models.DateField(verbose_name='Дата регистрации', null=True, blank=True)
    # ext_number          = models.CharField(max_length=100, verbose_name='Номер контрагента', null=True, blank=True)
    # sed_project_number  = models.CharField(max_length=100, verbose_name='Проектный номер', null=True, blank=True)
    # title               = models.TextField(verbose_name='Содержание', null=False, blank=False)
    # link_sed            = models.URLField(verbose_name='Ссылка на договор в СЭД', blank=True, null=True)
    # system              = models.ForeignKey('isystems.iSystem', verbose_name='Система', default="", blank=True, null=True, related_name='contracts')
    # price               = models.CharField(max_length=100, verbose_name='Полная стоимость договора (с НДС)', null=True, blank=True)
    # price               = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
#    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
#    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
#    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
#    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def _get_date_begin(self):
        try:
            return self.steps.earliest('date_begin').date_begin
        except:
            return ''
    date_begin = property(_get_date_begin)
    
    def _get_date_end(self):
        try:
            return self.steps.latest('date_end').date_end
        except:
            return ''
    date_end = property(_get_date_end)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['system']
        verbose_name = 'План-график'
        verbose_name_plural = 'План-графики'

class Step(MPTTModel):
    schedule        = models.ForeignKey('Schedule', verbose_name='План-график', blank=False, null=False, related_name='steps')
    step_num        = models.PositiveSmallIntegerField(verbose_name='Номер этапа', default='', null=True, blank=True)
    title           = models.TextField(verbose_name='Этап', default='', null=False, blank=False)
    milestone       = models.BooleanField(verbose_name='Важный этап', default=False)
    date_begin      = models.DateField(verbose_name='Дата начала', null=True, blank=True)
    date_end        = models.DateField(verbose_name='Дата завершения', null=True, blank=True)
    org_executors   = models.ManyToManyField('organizations.Organization', verbose_name='Исполнители', blank=True)
    man_executors   = models.ManyToManyField('people.People', verbose_name='Исполнители', blank=True)
    parent          = TreeForeignKey('self', verbose_name='Родительский этап', null=True, blank=True, related_name='children', db_index=True)
    done            = models.BooleanField(verbose_name='Этап завершен', default=False)
    report          = models.TextField(verbose_name='Результат этапа', default='', null=True, blank=True)
    
    def __str__(self):
        return '{}. {}'.format(self.step_num, self.title)

    class Meta:
        ordering = ['date_begin', '-date_end']
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
        
    class MPTTMeta:
        order_insertion_by = ['schedule']

mptt.register(Step, )
        
class ExecutorOrg(models.Model):
    executor    = models.ForeignKey('organizations.Organization', verbose_name='Исполнитель', blank=False, null=False, related_name='executor_orgs')
    step        = models.ForeignKey('Step', verbose_name='Этап', null=False, blank=False, related_name='executor_orgs')
    
    
    
# class Status(models.Model):
#     status          = models.CharField(max_length=100, verbose_name='Статус', default='в промышленной эксплуатации', null=False, blank=False)
#     system          = models.ForeignKey(iSystem, verbose_name='Система', blank=False, null=False, related_name='statuses')
#     status_date     = models.DateField(verbose_name='Дата присвоения статуса', blank=True, null=True)
#     # full_name       = models.CharField(max_length=150, verbose_name='Полное название', default='АИС', null=True, blank=True)
#     # description     = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
# #    group           = models.ForeignKey('grps.Group', verbose_name='Объект', default="", blank=False, related_name='messages')
# #    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
# #    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
# #    date_create     = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
# #    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
# #    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)
#
#     def __str__(self):
#         return self.status
#
#     class Meta:
#         ordering = ['system', '-status_date']
#         verbose_name = 'Статус'
#         verbose_name_plural = 'Статусы'
