from .models import Funcionario
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# Create your views here.
class FuncionarioListView(ListView):
    model = Funcionario
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEditView(UpdateView):
    model = Funcionario
    fields = ['nome', 'setor']

