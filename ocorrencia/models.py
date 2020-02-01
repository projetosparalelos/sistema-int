from django.db import models
from core.models import TimeStampedModel, CreatedBy
from pessoa.models import Pessoa, Veiculo


class Natureza(models.Model):
    natureza = models.TextField(unique=True)

    class Meta:
        ordering = ('natureza',)
        verbose_name = 'natureza'
        verbose_name_plural = 'naturezas'

    def __str__(self):
        return self.natureza


class Arma(models.Model):
    arma = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('arma',)
        verbose_name = 'arma'
        verbose_name_plural = 'armas'

    def __str__(self):
        return self.arma


class Infracao(CreatedBy, TimeStampedModel):
    QUALIFICACAO = (
        ('aut', 'Autor'),
        ('coaut', 'Co-Autor'),
        ('part', 'Participe'),
        ('vit', 'Vitima')
    )
    STATUS = (
        ('vivo', 'Vivo'),
        ('morto', 'Morto'),
        ('preso', 'Preso'),
        ('solto', 'Solto')
    )
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
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
        max_length=5,
        choices=STATUS,
        default='vivo'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'infração'
        verbose_name_plural = 'infrações'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class Ocorrencia(CreatedBy, TimeStampedModel):
    rai = models.IntegerField(null=True, blank=True)
    data_do_fato = models.DateField('Data do Fato')
    descricao = models.TextField('descrição', null=True, blank=True)

    class Meta:
        ordering = ('rai',)
        verbose_name = 'ocorrência'
        verbose_name_plural = 'ocorrências'

    def __str__(self):
        return str(self.rai)


class PessoaOcorrencia(CreatedBy, TimeStampedModel):
    '''
    Uma pessoa pode ter várias ocorrências.
    '''
    pessoa = models.ForeignKey(
        Pessoa,
        related_name='pessoas_ocorrencias',
        on_delete=models.CASCADE,
    )
    ocorrencia = models.ForeignKey(
        Ocorrencia,
        related_name='ocorrencias1',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.ocorrencia}'


class OcorrenciaVeiculo(CreatedBy, TimeStampedModel):
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