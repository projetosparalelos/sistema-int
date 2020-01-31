from django.contrib import admin
from .models import Arma
from .models import Comparsa
from .models import Cor
from .models import Faccao
from .models import Infracao
from .models import Modelo
from .models import Natureza
from .models import Ocorrencia
from .models import OcorrenciaVeiculo
from .models import Pessoa
from .models import PessoaContato
from .models import PessoaFoto
from .models import PessoaOcorrencia
from .models import PessoaVeiculo
from .models import Tatuagem
from .models import Veiculo


class InfracaoInline(admin.TabularInline):
    model = Infracao
    extra = 0


class PessoaOcorrenciaInline(admin.TabularInline):
    model = PessoaOcorrencia
    extra = 0


class PessoaContatoInline(admin.TabularInline):
    model = PessoaContato
    extra = 0


class ComparsaInline(admin.TabularInline):
    model = Comparsa
    extra = 0


class PessoaVeiculoInline(admin.TabularInline):
    model = PessoaVeiculo
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = (
        InfracaoInline,
        PessoaOcorrenciaInline,
        PessoaContatoInline,
        ComparsaInline,
        PessoaVeiculoInline
    )
    list_display = ('__str__', 'nome', 'sobrenome', 'apelido', 'faccao')
    search_fields = ('nome', 'sobrenome', 'apelido', 'mae', 'pai')
    list_filter = ('faccao',)


@admin.register(PessoaContato)
class PessoaContatoAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'pessoa')
    search_fields = ('pessoa__nome', 'telefone')


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('arma',)


@admin.register(Comparsa)
class ComparsaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('nome_comparsa',)


@admin.register(Tatuagem)
class TatuagemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = (
        'pessoa__nome',
        'pessoa__sobrenome',
        'pessoa__apelido',
        'descricao'
    )


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('natureza',)


@admin.register(Faccao)
class FaccaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'funcao')
    search_fields = ('nome',)
    list_filter = ('funcao',)


class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 0


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_do_fato')
    search_fields = ('rai', 'descricao')


# @admin.register(PessoaOcorrencia)
# class PessoaOcorrenciaAdmin(admin.ModelAdmin):
#     inlines = (OcorrenciaInline,)
#     list_display = ('__str__',)
#     # search_fields = ('',)


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'cor')
    search_fields = ('placa', 'modelo__modelo', 'cor')
    list_filter = ('modelo', 'cor')


@admin.register(PessoaVeiculo)
class PessoaVeiculoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    # search_fields = ('',)


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('modelo',)


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('cor',)


admin.site.register(PessoaFoto)
