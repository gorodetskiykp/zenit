from django.db import models

class People(models.Model):
    fio     = models.CharField(max_length=250, verbose_name='Фамилия Имя Отчество', default='', null=False, blank=False)
    info    = models.TextField(verbose_name='Дополнительная информация', default='', null=True, blank=True)
    # post            = models.CharField(max_length=250, verbose_name='Должность', default='', null=True, blank=True)
    # organizations   = models.ManyToManyFields('organizations.Organization', verbose_name='Организации', default="", null=True, blank=True, related_name='people')
    # email           = models.EmailField(max_length=100, verbose_name='Основной ', default='', null=False, blank=False)
    #    category        = models.ForeignKey(Category, verbose_name='Категория', blank=False, related_name='messages')
#    date_create     = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
#    date_updated    = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
#    photo           = models.ImageField(upload_to=upload_location, null=True, blank=True)

    @property
    def short_fio(self):
        try:
            fio = self.fio.split()
            return '{} {}.{}.'.format(fio[0], fio[1][0], fio[2][0])
        except:
            return ' - '

    def __str__(self):
        return self.fio

    @property
    def is_system_admin(self):
        roles = self.org_roles.all()
        systems = []
        for role in roles:
            for system in role.administrator_systems.all():
                if system.short_name:
                    return True
        return False

    class Meta:
        ordering = ['fio']
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

class Emails(models.Model):
    email       = models.EmailField(max_length=100, verbose_name='email', default='@', null=False, blank=False)
    people      = models.ForeignKey(People, verbose_name='Работник', default="", null=False, blank=False, related_name='emails')
    base_mail   = models.BooleanField(verbose_name='Основной адрес', default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'email'
        verbose_name_plural = 'emails'

class Phone_Type(models.Model):
    phone_type = models.CharField(max_length=100, verbose_name='Тип телефонной связи', null=False, blank=False)

    def __str__(self):
        return self.phone_type

    class Meta:
        ordering = ['phone_type']
        verbose_name = 'Тип телефонной связи'
        verbose_name_plural = 'Типы телефонной связи'

class Phone(models.Model):
    people          = models.ForeignKey(People, verbose_name='Работник', default="", null=False, blank=False, related_name='phones')
    phone_number    = models.CharField(max_length=100, verbose_name='Номер телефона', default='', null=False, blank=False)
    phone_type      = models.ForeignKey(Phone_Type, verbose_name='Тип телефонной связи', default='', null=True, blank=True, related_name='phones')

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ['phone_number']
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Organization_Based_Role(models.Model):
    people          = models.ForeignKey(People, verbose_name='Работник', default="", null=False, blank=False, related_name='org_roles')
    organization    = models.ForeignKey('organizations.Organization', verbose_name='Организация', default="", null=False, blank=False, related_name='org_roles')
    post            = models.CharField(max_length=250, verbose_name='Должность', default='', null=False, blank=False)

    def __str__(self):
        return '{} - {} {}'.format(self.people, self.post, self.organization)

    class Meta:
        ordering = ['people']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class System_Based_Role(models.Model):
    people  = models.ForeignKey(Organization_Based_Role, verbose_name='Работник', default="", null=False, blank=False, related_name='sys_roles')
    system  = models.ForeignKey('isystems.iSystem', verbose_name='Система', default="", null=False, blank=False, related_name='sys_roles')
    role    = models.CharField(max_length=250, verbose_name='Роль', default='', null=False, blank=False)

    def __str__(self):
        return '{} - {}. {}'.format(self.people, self.system, self.role)

    class Meta:
        ordering = ['people', 'system']
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
