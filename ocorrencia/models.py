from django.db import models
from django.urls import reverse_lazy
from core.models import UuidModel, TimeStampedModel, CreatedBy, Address
from pessoa.models import Pessoa, Veiculo
from utils.data import QUALIFICACAO, STATUS


class Natureza(UuidModel):
    natureza = models.TextField(unique=True)

    class Meta:
        ordering = ('natureza',)
        verbose_name = 'natureza'
        verbose_name_plural = 'naturezas'

    def __str__(self):
        return self.natureza

    def get_absolute_url(self):
        return reverse_lazy('ocorrencia:naturezas')

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.natureza,
        }


class Arma(UuidModel):
    arma = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('arma',)
        verbose_name = 'arma'
        verbose_name_plural = 'armas'

    def __str__(self):
        return self.arma

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.arma,
        }


class Infracao(UuidModel, CreatedBy, TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True)
    natureza = models.ForeignKey(
        Natureza,
        on_delete=models.SET_NULL,
        verbose_name='natureza',
        related_name='naturezas',
        null=True,
        blank=True
    )
    qualificacao = models.CharField(
        max_length=5,
        choices=QUALIFICACAO,
        default='aut',
    )
    arma = models.ForeignKey(
        Arma,
        on_delete=models.SET_NULL,
        verbose_name='arma de fogo',
        related_name='armas',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS,
        default='foragido'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'infração'
        verbose_name_plural = 'infrações'

    def __str__(self):
        return f'{self.pessoa} - {self.natureza}'

    def get_absolute_url(self):
        return reverse_lazy('ocorrencia:infracoes')


class Ocorrencia(UuidModel, CreatedBy, TimeStampedModel):
    rai = models.IntegerField(null=True, blank=True)
    data_do_fato = models.DateField('Data do Fato')
    descricao = models.TextField('descrição', null=True, blank=True)

    class Meta:
        ordering = ('rai',)
        verbose_name = 'ocorrência'
        verbose_name_plural = 'ocorrências'

    def __str__(self):
        return str(self.rai)

    def get_absolute_url(self):
        return reverse_lazy('ocorrencia:ocorrencia', kwargs={'pk': self.pk})

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.rai,
        }


class PessoaOcorrencia(UuidModel, CreatedBy, TimeStampedModel):
    '''
    Uma pessoa pode ter várias ocorrências.
    '''
    pessoa = models.ForeignKey(
        Pessoa,
        related_name='pessoas_ocorrencias',
        on_delete=models.CASCADE,
        blank=True
    )
    ocorrencia = models.ForeignKey(
        Ocorrencia,
        related_name='ocorrencias1',
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.ocorrencia}'


class OcorrenciaVeiculo(UuidModel, CreatedBy, TimeStampedModel):
    '''
    Uma ocorrência pode ter vários veículos.
    '''
    ocorrencia = models.ForeignKey(
        'Ocorrencia',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.ocorrencia} - {self.veiculo}'


class AreaUpm(UuidModel, models.Model):
    area_upm = models.CharField('área UPM', max_length=50, unique=True)

    class Meta:
        ordering = ('area_upm',)
        verbose_name = 'area upm'
        verbose_name_plural = 'area upms'

    def __str__(self):
        return self.area_upm


class Motivacao(UuidModel, models.Model):
    titulo = models.CharField('título', max_length=50, unique=True)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'motivação'
        verbose_name_plural = 'motivações'

    def __str__(self):
        return self.titulo


FORMA = (
    ('tentado', 'Tentado'),
    ('consumado', 'Consumado'),
)


class Homicidio(UuidModel, Address, CreatedBy, TimeStampedModel):
    rai = models.ForeignKey(
        Ocorrencia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data_do_homicidio = models.DateField('Data do Homicídio')
    forma = models.CharField(max_length=10, choices=FORMA, default='tentado')
    area_upm = models.ForeignKey(AreaUpm, on_delete=models.CASCADE)
    vitima = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(
        Arma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    motivacao = models.ForeignKey(Motivacao, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-data_do_homicidio',)
        verbose_name = 'homicídio'
        verbose_name_plural = 'homicídios'

    def __str__(self):
        return str(self.rai)

    def get_absolute_url(self):
        return reverse_lazy('ocorrencia:homicidios')
