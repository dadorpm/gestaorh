from django.urls import path
from .views import FuncionarioListView, FuncionarioEditView, FuncionarioDeleteView

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('edita/<int:pk>/', FuncionarioEditView.as_view(), name='edita_funcionario'),
    path('apaga/<int:pk>/', FuncionarioDeleteView.as_view(), name='apaga_funcionario'),
]
