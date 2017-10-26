from django.db import models


class Plan(models.Model):
    PLAN_STATUSES = (
    ('rdy', 'Утвержден в работу'),
    ('pro', 'Проект')
    )
    year        = models.CharField(max_length=4, verbose_name='Год', default='20', null=False, blank=False)
    status      = models.CharField(max_length=3, choices=PLAN_STATUSES, verbose_name='статус', default='pro', null=False, blank=False)
    base_plan   = models.ForeignKey('Plan', verbose_name='Основной план, если это изм', null=True, blank=True, related_name='plans')
    ism_no      = models.PositiveSmallIntegerField(verbose_name='Номер изм, если это изм', default=0, null=False, blank=False)
    # organizations   = models.ManyToManyFields('organizations.Organization', verbose_name='Организации', default="", null=True, blank=True, related_name='people')
    # email           = models.EmailField(max_length=100, verbose_name='Основной ', default='', null=False, blank=False)
    #    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
#    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
#    date_create     = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
#    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
#    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.year

    class Meta:
        ordering = ['-year']
        verbose_name = 'План поставок'
        verbose_name_plural = 'Планы поставок'
