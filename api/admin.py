from django.contrib import admin
from .models import Categoria,Post,Foto

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('titulo','activo')

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo','posteado','categoria','posteable')

class FotoAdmin(admin.ModelAdmin):
	list_display = ('post','imagen')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Foto, FotoAdmin)
