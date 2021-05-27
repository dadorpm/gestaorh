from django.db import models


class empresa(models.Model):
    nome = models.CharField(max_length=150, help_text='nome da empresa')
