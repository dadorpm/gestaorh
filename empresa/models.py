from django.db import models
from django.shortcuts import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=150, help_text='nome da empresa')

    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('home')
