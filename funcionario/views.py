from .models import Funcionario
from django.views.generic.list import ListView

# Create your views here.
class FuncionarioListView(ListView):
    model = Funcionario