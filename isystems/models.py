import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

from django.db.models import (
    Model,
    BooleanField as BF,
    CharField as CF,
    DateField as DF,
    ForeignKey as FK,
    TextField as TF,
    URLField as UF,
)

from multiselectfield import MultiSelectField
from positions import PositionField


class iSystem(models.Model):
    SYSTEM_TYPES = (
        ('Локальная', 'Локальная'),
        ('Корпоративная', 'Корпоративная'),
    )

    SYSTEM_FUNCTIONS = (
        ('Автоматизированная система', (
            ('Автоматизированная производственная система', 'Производственная система',),
            ('Автоматизированная административная система', 'Административная система'),
            ('Автоматизированная финансовая (учетая) система', 'Финансовая (учетая) система'),
            ('Автоматизированная система маркетинга', 'Система маркетинга'),
            ('Автоматизированная система научных исследований', 'Система научных исследований'),
        )),
        ('Система поддержки принятия решений', (
            ('Система поддержки принятия решений руководителя', 'Руководителя'),
            ('Система поддержки принятия решений должностного лица органа управления',
             'Должностного лица органа управления'),
            ('Система поддержки принятия решений оперативного дежурного', 'Оперативного дежурного'),
            ('Система поддержки принятия решений оператора', 'Оператора'),
        )),
        ('Информационно-вычислительная система', (
            ('Информационно-расчетная система', 'Информационно-расчетная система'),
            ('Система автоматизированного проектирования',
             'Система автоматизированного проектирования'),
            ('Моделирующая система', 'Моделирующая система'),
            ('Проблемно-ориентированная система', 'Проблемно-ориентированная система'),
        )),
        ('Информационно-справочная система', (
            ('Система делопроизводства', 'Система делопроизводства'),
            ('Автоматизированный архив', 'Автоматизированный архив'),
            ('Система ведения электронных карт местности', 'Система ведения электронных карт местности'),
            ('Справочная картотека', 'Справочная картотека'),
        )),
        ('Cистема обучения', (
            ('Система программного обучения', 'Система программного обучения'),
            ('Система обеспечения деловых игр', 'Система обеспечения деловых игр'),
            ('Тренажер (тренажерный комплекс)', 'Тренажер (тренажерный комплекс)'),
            ('Система управления образованием', 'Система управления образованием'),
        )),
    )

    INFO_CATEGORY = (
        ('К', 'Конфиденциальная'),
        ('КТ', 'Коммерческая тайна'),
        ('ПДн', 'Персональные данные'),
        ('ДСП', 'Для служебного пользования'),
    )

    FUNCTIONAL_CUSTOMER = (
        ('Все отделы и службы', 'Все отделы и службы'),
        ('ОГМетр', 'Отдел главного метролога'),
        ('ОИТ', 'Отдел информационных технологий'),
        ('ОК', 'Отдел кадров'),
        ('ОМ', 'Отдел мониторинга'),
        ('ООП', 'Отдел общественного питания'),
        ('ОПиПТ', 'Отдел планирования и проведения торгов'),
        ('СОК', 'Служба общественных коммуникаций'),
        ('СОТ', 'Служба охраны труда'),
        ('ТТО', 'Товарно-транспортная служба'),
        ('ЮО', 'Юридический отдел'),
    )

    short_name = CF('Краткое название', max_length=100, default='', unique=True, null=False, blank=False)
    full_name = CF('Полное название', max_length=500, default='', null=True, blank=True)
    abbreviation = CF('Аббревиатура', max_length=20, null=False, blank=False, unique=True, help_text='Латинскими прописными буквами, допускается символ подчеркивания')
    project = FK('Project', verbose_name='Проект', default='', blank=True, null=True,
                                related_name='project_systems')
    system_type = CF('Тип системы', max_length=20, choices=SYSTEM_TYPES, default='Локальная', null=True,
                                   blank=True)
    system_function = CF('Назначение системы', max_length=50, choices=SYSTEM_FUNCTIONS, default='',
                                       null=True, blank=True)

    developer = FK('organizations.Organization', verbose_name='Разработчик', default='', blank=True,
                                  null=True, related_name='systems')
    maintenance = models.ForeignKey('organizations.Organization', verbose_name='Техническое сопровождение', default='', blank=True,
                                  null=True, related_name='ment_systems')
    # rightowner      = models.ForeignKey('organizations.Organization', verbose_name='Правообладатель', default='', blank=True, null=True, related_name='systems')
    description = models.TextField('Описание', default='', blank=True, null=True)
    support_info = models.TextField('Информация о технической поддержке', blank=True, null=True)
    lic_info = models.TextField('Информация о лицензировании', blank=True, null=True)

    info_category = MultiSelectField('Категории обрабатываемой информации', max_length=20, choices=INFO_CATEGORY, default='', null=True,
                                   blank=True)

    administrator = models.ForeignKey('people.Organization_Based_Role', verbose_name='Администратор', default='', null=True,
                                      blank=True, related_name='administrator_systems')
    reserve_administrator = models.ForeignKey('people.Organization_Based_Role', verbose_name='Резервный администратор', default='', null=True,
                                      blank=True, related_name='reserve_administrator_systems')
    contract_administrator = models.ForeignKey('people.Organization_Based_Role', verbose_name='Ответственный за договоры и бюджет',
                                              default='', null=True,
                                              blank=True, related_name='contract_administrator_systems')
    isecurity_administrator = models.ForeignKey('people.Organization_Based_Role', verbose_name='Ответственный за информационную безопасность',
                                              default='', null=True,
                                              blank=True, related_name='isecurity_administrator_systems')

    critical = BF('Критичность для функционирования организации', default=False)
    functional_customer = MultiSelectField('Функциональные заказчики', max_length=20, choices=FUNCTIONAL_CUSTOMER,
                                     default='', null=True,
                                     blank=True)

    upgrade_order = TF('Порядок обновления', blank=True, null=True)
    recovery_order = TF('Порядок восстановления', blank=True, null=True)
    test_procedure = TF('Порядок тестирования', blank=True, null=True)

    shadow = BF('Теневая система', default=False, help_text='ИТ-устройства, ПО и сервисы, которые присутствуют в организации, но не обслуживаются ИТ-отделом.')
    responsibility_center = FK('organizations.ResponsibilityCenter', verbose_name='Ответственный за сопровождение', default='', blank=True,
                              null=True)

    def __str__(self):
        return self.short_name


    @property
    def all_names(self):
        return '{} ({})'.format(self.short_name, self.full_name)


    @property
    def administrators(self):
        # return '{} {} {} {}'.format(
        #     self.administrator.people.fio,
        #     self.reserve_administrator.people.fio,
        #     self.contract_administrator.people.fio,
        #     self.isecurity_administrator.people.fio)

        def get_administrator_fio(administrator):
            try:
                fio = administrator.people.fio.split()
                return '{} {}.{}.'.format(fio[0], fio[1][0], fio[2][0])
            except:
                return ' - '

        return '{};{};{};{}'.format(
            get_administrator_fio(self.administrator),
            get_administrator_fio(self.reserve_administrator),
            get_administrator_fio(self.contract_administrator),
            get_administrator_fio(self.isecurity_administrator)
        )

    @property
    def info_categories(self):
        return ', '.join(self.info_category)

    @property
    def functional_customers(self):
        return ', '.join(self.functional_customer)


    class Meta:
        ordering = ['short_name']
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'


class Life_Step(Model):
    step = CF(max_length=200, verbose_name='Этап жизненного цикла ИС', null=False, blank=False)
    position = PositionField(verbose_name='Порядковый номер', default=0)

    def __str__(self):
        return self.step


    class Meta:
        ordering = ['position', 'step']
        verbose_name = 'Этап жизненного цикла ИС'
        verbose_name_plural = 'Этапы жизненного цикла ИС'


class Status(models.Model):
    SYSTEM_STATUSES = (
        ('в опытной эксплуатации', 'в опытной эксплуатации'),
        ('завершена опытная эксплуатация', 'завершена опытная эксплуатация'),
        ('в промышленной эксплуатации', 'в промышленной эксплуатации'),
        ('первичная закупка', 'первичная закупка'),

    )

    status = models.CharField(max_length=100, verbose_name='Статус', choices=SYSTEM_STATUSES,
                              default='в промышленной эксплуатации', null=False, blank=False)
    system = models.ForeignKey(iSystem, verbose_name='Система', blank=False, null=False, related_name='statuses')
    status_date = models.DateField(verbose_name='Дата присвоения статуса', blank=True, null=True)
    link_eatd = models.URLField(verbose_name='Ссылка на отчетный документ', blank=True, null=True)

    # full_name       = models.CharField(max_length=150, verbose_name='Полное название', default='АИС', null=True, blank=True)
    # description     = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
    #    group           = models.ForeignKey('grps.Group', verbose_name='Объект', default="", blank=False, related_name='messages')
    #    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
    #    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
    #    date_create     = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    #    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    #    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['system', '-status_date']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Проект', null=False, blank=False)

    # system          = models.ForeignKey(iSystem, verbose_name='Система', blank=False, null=False, related_name='statuses')
    # status_date     = models.DateField(verbose_name='Дата присвоения статуса', blank=True, null=True)
    # link_eatd       = models.URLField(verbose_name='Ссылка на отчетный документ в ЭАТД', blank=True, null=True)
    # full_name       = models.CharField(max_length=150, verbose_name='Полное название', default='АИС', null=True, blank=True)
    # description     = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
    #    group           = models.ForeignKey('grps.Group', verbose_name='Объект', default="", blank=False, related_name='messages')
    #    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
    #    message_text    = models.TextField(verbose_name='Замечание', help_text='Замечание')
    #    date_create     = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    #    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    #    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
