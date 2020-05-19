from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Categorias(models.TextChoices):
    GR = 'GR', 'Geral'
    EVT = 'EVT', 'Eventos'
    CUL = 'CUL', 'Cultos'
    CR = 'CR', 'Curiosidades'
    PB = 'PB', 'Passagens Bíblicas'

class Contato(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Post(models.Model):
    titulo = RichTextField()
    sub_titulo = models.CharField(max_length=200)
    conteudo = RichTextUploadingField()
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