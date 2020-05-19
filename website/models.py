from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    GR = 'GR', 'Geral'
    EVT = 'EVT', 'Eventos'
    CUL = 'CUL', 'Cultos'
    CR = 'CR', 'Curiosidades'
    PB = 'PB', 'Passagens Bíblicas'

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    categorias = models.CharField(
        max_length=4,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    imagem = models.ImageField(upload_to='posts', null=True, blank=True)

    def get_categoty_label(self):
        return self.get_categorias_display()


    def __str__(self):
        return self.titulo