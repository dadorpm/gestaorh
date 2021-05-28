from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome']
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEditView(UpdateView):
    model = Empresa
    fields = ['nome']
