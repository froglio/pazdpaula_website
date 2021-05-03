from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField(
        max_length=100
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    #conteudo = models.TextField()
    conteudo = RichTextField()

    criado = models.DateTimeField(
        auto_now_add=True
    )


    # def __str__(self):
    #     publicado_convertido = self.publicado.strftime("%d/%m/%Y %H:%M:%S")
    #     return "{} - {}".format(self.titulo, publicado_convertido)
    
