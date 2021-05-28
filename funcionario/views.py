from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Funcionario
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


# Create your views here.
class FuncionarioListView(ListView):
    model = Funcionario
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEditView(UpdateView):
    model = Funcionario
    fields = ['nome', 'setor']
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('lista_funcionarios')
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'setor']
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create_user(username=funcionario.nome)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)