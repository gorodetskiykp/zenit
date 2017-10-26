from django.db.models import (
    Model,
    CharField as CF,
    DateField as DF,
    ForeignKey as FK,
    URLField as UF,
)


class Document_Type(Model):
    doc_type = CF(max_length=150, verbose_name='Тип документа', default='')

    def __str__(self):
        return self.doc_type


    class Meta:
        ordering = ['doc_type']
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'


class Document(Model):
    doc_date = DF(verbose_name='Дата документа', blank=True, null=True)
    doc_type = FK(Document_Type, verbose_name='Тип документа', blank=True, null=True, related_name='type_documents')
    doc_name = CF(max_length=500, verbose_name='Название документа', default='')
    creator = FK('organizations.Organization', verbose_name='Создатель документа', blank=True, null=True, related_name='org_documents')
    doc_link = UF(verbose_name='Ссылка на документ', blank=True, null=True)

    def __str__(self):
        return self.doc_name


    class Meta:
        ordering = ['doc_name']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
