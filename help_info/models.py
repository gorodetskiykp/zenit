from django.db.models import (
    Model,
    CharField as CF,
    DateField as DF,
    ForeignKey as FK,
    URLField as UF,
    TextField as TF,
    DateTimeField as DTF,
)

class WhatsNew(Model):
    whats_new_message = TF(verbose_name='Что нового')
    release_date_time = DTF(auto_now_add=True)

    def __str__(self):
        return self.whats_new_message

    class Meta:
        ordering = ['-release_date_time']
        verbose_name = 'Что нового'
        verbose_name_plural = 'Что нового'