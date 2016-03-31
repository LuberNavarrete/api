from rest_framework.serializers import ModelSerializer
from .models import Categoria, Post, Foto

class CategoriaSerializer(ModelSerializer):
	class Meta:
		model = Categoria
		# fields = ('id','titulo','activo')

class PostSerializer(ModelSerializer):

	categoria = CategoriaSerializer(many = False)

	class Meta:
		model = Post
		# fields = ('id','titulo','texto','posteado','fecha_inicio','fecha_fin','categoria','posteable')

class FotoSerializer(ModelSerializer):

	post = PostSerializer(many = False)

	class Meta:
		model = Foto
		# fields = ('post','imagen')
