from django.contrib import admin
from .models import Categoria,Post,Foto

class FotoInline(admin.StackedInline):
    model = Foto
    extra = 3

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('titulo','activo')

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo','posteado','categoria','posteable')
	inlines = [FotoInline]

# class FotoAdmin(admin.ModelAdmin):
	# list_display = ('post','src')
	

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Foto, FotoAdmin)
