from django.db import models

from django.db.models import (
    Model,
    CharField as CF,
    DateField as DF,
    ForeignKey as FK,
    URLField as UF,
)

class Organization(models.Model):
    short_name      = models.CharField(max_length=200, verbose_name='Краткое название', default='', null=False, blank=False, unique=True)
    full_name       = models.CharField(max_length=200, verbose_name='Полное название', default='', null=False, blank=False)
    phones          = models.CharField(max_length=100, verbose_name='Телефоны', default='', null=True, blank=True)
    faxes           = models.CharField(max_length=100, verbose_name='Факсы', default='', null=True, blank=True)
    sites           = models.CharField(max_length=300, verbose_name='Сайт', default='', null=True, blank=True)
    emails          = models.CharField(max_length=100, verbose_name='emails', default='', null=True, blank=True)
    inn             = models.CharField(max_length=50, verbose_name='ИНН', default='', null=True, blank=True)
    rs              = models.CharField(max_length=200, verbose_name='Р/с №', default='', null=True, blank=True)
    ks              = models.CharField(max_length=200, verbose_name='К/с №', default='', null=True, blank=True)
    bik             = models.CharField(max_length=50, verbose_name='БИК', default='', null=True, blank=True)
    kpp             = models.CharField(max_length=50, verbose_name='КПП', default='', null=True, blank=True)
    okpo	        = models.CharField(max_length=50, verbose_name='ОКПО', default='', null=True, blank=True)
    ogrn	        = models.CharField(max_length=50, verbose_name='ОГРН', blank=True, null=True)
    official_info   = models.URLField(verbose_name='Карточка организации', default='', null=True, blank=True)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['short_name']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class OrgAddress(models.Model):
    organization = models.ForeignKey('Organization', verbose_name='Организация', blank=False, related_name='addresses')
    address = models.TextField(verbose_name='Адрес', blank=False)
    address_type = models.ForeignKey('AddressType', verbose_name='Тип адреса', blank=False, related_name='addresses')
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
    

class AddressType(models.Model):
    address_type = models.CharField(max_length=50, verbose_name='Тип адреса', default='', null=False, blank=False)
    
    def __str__(self):
        return self.address_type
        
    class Meta:
        verbose_name = 'Тип адреса'
        verbose_name_plural = 'Типы адресов'


class Department(Model):
    short_name = CF(max_length=50, verbose_name='Краткое название', unique=True)
    full_name = CF(max_length=200, verbose_name='Полное название', unique=True)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['short_name', 'full_name']
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        

class ResponsibilityCenter(Model):
    short_name = CF(max_length=50, verbose_name='Краткое название', unique=True)
    full_name = CF(max_length=200, verbose_name='Полное название', unique=True)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['short_name', 'full_name']
        verbose_name = 'Центр ответственности'
        verbose_name_plural = 'Центр ответственности'


