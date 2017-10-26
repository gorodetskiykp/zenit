import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

class Contract(models.Model):
    sed_number          = models.CharField(max_length=100, verbose_name='Внутренний номер', null=True, blank=True)
    reg_date            = models.DateField(verbose_name='Дата регистрации', null=True, blank=True)
#    ext_number          = models.CharField(max_length=100, verbose_name='Номер контрагента', null=True, blank=True)
    contractor          = models.ForeignKey('organizations.Organization', verbose_name='Контрагент', default='', blank=True, null=True, related_name='contracts')
    title               = models.TextField(verbose_name='Содержание', null=False, blank=False)
    link_sed            = models.URLField(verbose_name='Ссылка на договор в СЭД', blank=True, null=True)
    system              = models.ForeignKey('isystems.iSystem', verbose_name='Система', default="", blank=True, null=True, related_name='contracts')
    start_date          = models.DateField(verbose_name='Действует с', null=True, blank=True)
    end_date            = models.DateField(verbose_name='Действует по', null=True, blank=True)
    cost                = MoneyField(verbose_name='Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')
    nds                 = MoneyField(verbose_name='в т.ч. НДС 18%', max_digits=10, decimal_places=2, default_currency='RUB')
    # price               = models.CharField(max_length=100, verbose_name='Полная стоимость договора (с НДС)', null=True, blank=True)
    # price               = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
#    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
#    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
#    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
#    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.sed_number, self.title)

    class Meta:
        ordering = ['reg_date', 'title']
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

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
