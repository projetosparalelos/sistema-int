from django.urls import path, include
from veiculo import views as v


app_name = 'veiculo'


veiculo_patterns = [
    path('', v.veiculos, name="veiculos"),
    path('add/', v.veiculo_create, name="veiculo_create"),
    path('<int:pk>/upate/', v.VeiculoUpdate.as_view(), name="veiculo_update"),
]

modelo_patterns = [
    path('', v.modelos, name="modelos"),
    path('add/', v.modelo_create, name="modelo_create"),
]


urlpatterns = [
    path('veiculo/', include(veiculo_patterns)),
    path('modelo/', include(modelo_patterns)),
]
