from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    connection = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=50, verbose_name='Название документа')
    description = models.TextField(max_length=100, verbose_name='Краткое описание документа')
    document = models.FileField(verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['name']

    def __str__(self):
        return self.name
