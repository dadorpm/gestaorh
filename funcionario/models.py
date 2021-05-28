from django.db import models
from django.contrib.auth.models import User
from setor.models import Setor
from empresa.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    setor = models.ManyToManyField(Setor)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.nome