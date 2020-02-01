from django.db import models
from core.models import TimeStampedModel


class Veiculo(TimeStampedModel):
    placa = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.ForeignKey(
        'Modelo',
        on_delete=models.PROTECT,
        related_name='modelos',
    )
    cor = models.ForeignKey(
        'Cor',
        on_delete=models.PROTECT,
        related_name='cores',
    )

    class Meta:
        ordering = ('placa',)
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return f'{self.placa} - {self.modelo} - {self.cor}'


class Modelo(models.Model):
    modelo = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ('modelo',)
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return self.modelo


class Cor(models.Model):
    cor = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('cor',)
        verbose_name = 'cor'
        verbose_name_plural = 'cores'

    def __str__(self):
        return self.cor