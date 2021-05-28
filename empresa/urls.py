from django.urls import path
from empresa.views import EmpresaCreateView, EmpresaEditView

urlpatterns = [
    path('novo', EmpresaCreateView.as_view(), name='cria_empresa'),
    path('edita/<int:pk>/', EmpresaEditView.as_view(), name='edita_empresa'),
]
