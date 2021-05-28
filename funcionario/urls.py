from django.urls import path
from .views import FuncionarioListView, FuncionarioEditView, FuncionarioDeleteView, FuncionarioCreateView
urlpatterns = [
    path('', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('criar/', FuncionarioCreateView.as_view(), name='criar_funcionario'),
    path('edita/<int:pk>/', FuncionarioEditView.as_view(), name='edita_funcionario'),
    path('apaga/<int:pk>/', FuncionarioDeleteView.as_view(), name='apaga_funcionario'),
]
