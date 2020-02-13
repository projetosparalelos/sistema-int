from django.urls import path, include
from ocorrencia import views as v


app_name = 'ocorrencia'


ocorrencia_patterns = [
    path('', v.ocorrencias, name="ocorrencias"),
    path('<int:pk>/', v.ocorrencia, name="ocorrencia"),
    path('add/', v.ocorrencia_create, name="ocorrencia_create"),
]

infracao_patterns = [
    path('', v.infracoes, name="infracoes"),
    path('add/', v.infracao_create, name="infracao_create"),
]

natureza_patterns = [
    path('', v.naturezas, name="naturezas"),
    path('add/', v.natureza_create, name="natureza_create"),
]

homicidio_patterns = [
    path('', v.homicidios, name="homicidios"),
    path('add/', v.homicidio_create, name="homicidio_create"),
]

urlpatterns = [
    path('ocorrencia/', include(ocorrencia_patterns)),
    path('infracao/', include(infracao_patterns)),
    path('natureza/', include(natureza_patterns)),
    path('homicidio/', include(homicidio_patterns)),
]
