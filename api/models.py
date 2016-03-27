from __future__ import unicode_literals
# from django_autoslug.fields import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default = 'true')

    def __unicode__(self):
        return '%s' % self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    # slug = AutoSlugField(populate_from='title', unique_with='posteado')
    texto = models.TextField()
    posteado = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null = True, blank = True)
    fecha_fin = models.DateTimeField(null = True, blank = True)
    categoria = models.ForeignKey('Categoria',limit_choices_to={'activo': True})
    # propietario = models.ForeignKey(User)
    posteable = models.BooleanField(default = 'true')

    def __unicode__(self):
        return '%s' % self.titulo

class Foto(models.Model):
    post = models.ForeignKey(Post, related_name='Fotos')
    imagen = models.ImageField(upload_to="%Y/%m/%d")

    def __unicode__(self):
        return '%s' % self.post