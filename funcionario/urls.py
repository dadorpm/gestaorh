from django.urls import path
from .views import FuncionarioListView, FuncionarioEditView

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('edita/<int:pk>/', FuncionarioEditView.as_view(), name='edita_funcionario'),
]
