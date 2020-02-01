from django.db import models
from core.models import TimeStampedModel, CreatedBy, Address, Document


class Pessoa(TimeStampedModel, CreatedBy, Address, Document):
    nome = models.CharField('nome', max_length=50, null=True, blank=True)
    sobrenome = models.CharField(
        'sobrenome',
        max_length=100,
        null=True,
        blank=True,
    )
    apelido = models.CharField(max_length=50, null=True, blank=True)
    mae = models.CharField(max_length=50, null=True, blank=True)
    pai = models.CharField(max_length=50, null=True, blank=True)
    faccao = models.ForeignKey(
        'Faccao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return ' '.join(filter(None, [self.nome, self.sobrenome]))


class PessoaFoto(TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    fotopessoa = models.ImageField('Imagem da Pessoa', upload_to="pessoa")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class PessoaContato(TimeStampedModel):
    '''
    Telefones
    '''
    TIPO_TELEFONE = (
        ('cel', 'Celular'),
        ('tel', 'Telefone'),
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tipo_telefone = models.CharField(
        max_length=10,
        choices=TIPO_TELEFONE,
        default='cel'
    )
    telefone = models.CharField(max_length=50)

    class Meta:
        ordering = ('pessoa', 'telefone')
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return f'{self.pessoa} - {self.telefone}'


class Comparsa(TimeStampedModel, Document):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_comparsa = models.CharField(
        'nome',
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('pessoa', 'nome_comparsa')
        verbose_name = 'comparsa'
        verbose_name_plural = 'comparsas'

    def __str__(self):
        return self.nome_comparsa


class Tatuagem(TimeStampedModel):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    foto_tatuagem = models.ImageField(
        'Imagem da Tatuagem',
        upload_to="tatuagem"
    )
    descricao = models.TextField(
        'Descrição da Tatuagem',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('pessoa', '-created')
        verbose_name = 'tatuagem'
        verbose_name_plural = 'tatuagens'

    def __str__(self):
        return f'{self.pk} - {self.pessoa}'


class Faccao(models.Model):
    FUNCAO_CHOICES = (
        ('chefe', 'Chefe'),
        ('membro', 'Membro'),
    )
    nome = models.CharField(max_length=100, unique=True)
    funcao = models.CharField(
        max_length=10,
        choices=FUNCAO_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'facção'
        verbose_name_plural = 'facções'

    def __str__(self):
        return self.nome


class PessoaVeiculo(CreatedBy, TimeStampedModel):
    '''
    Uma pessoa pode ter vários veículos.
    '''
    pessoa = models.ForeignKey(
        'Pessoa',
        related_name='pessoas_veiculos',
        on_delete=models.CASCADE,
    )
    veiculo = models.ForeignKey(
        'Veiculo',
        related_name='veiculos2',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pessoa} - {self.veiculo}'


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
