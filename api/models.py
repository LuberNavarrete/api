from __future__ import unicode_literals
from django.template import defaultfilters
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

##Remueve tags de html
from django.utils.html import strip_tags

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default = 'true')

    def __unicode__(self):
        return '%s' % self.titulo

class Post(models.Model):
    categoria = models.ForeignKey('Categoria',limit_choices_to={'activo': True})
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,null = True, blank = True, editable = False)
    texto = HTMLField()
    posteado = models.DateField(auto_now_add=True)
    # fecha_inicio = models.DateTimeField(null = True, blank = True)
    # fecha_fin = models.DateTimeField(null = True, blank = True)
    # propietario = models.ForeignKey(User)
    resumen = models.CharField(max_length=100, null = True, blank = True, editable = False)
    posteable = models.BooleanField(default = 'true')

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo)
        self.resumen = strip_tags(self.texto)[:750] # Recorta la cadena
        self.resumen = self.resumen.replace('&nbsp;', ' ') # Espacio horizontal
        self.resumen = self.resumen.replace('acute;', '') # Espacio palabras con acento derecha
        self.resumen = self.resumen.replace('&', '') # Espacio palabras con acento izquierda
        self.resumen = self.resumen.replace('\r\n', ' ') # Salto de linea
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.titulo

class Foto(models.Model):
    post = models.ForeignKey(Post, related_name='Fotos')
    src = models.ImageField(upload_to="%Y/%m/%d")

    def __unicode__(self):
        return '%s' % self.post