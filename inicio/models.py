from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(
        max_length=100
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    conteudo = models.TextField()

    publicado = models.DateTimeField(
        default=timezone.now
    )


    def __str__(self):
        return "{} - {}".format(self.titulo, self.publicado)
    
