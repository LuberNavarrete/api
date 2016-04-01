from rest_framework.serializers import ModelSerializer
from .models import Categoria, Post, Foto

class CategoriaSerializer(ModelSerializer):

	class Meta:
		model = Categoria

class PostSerializer(ModelSerializer):

	class Meta:
		model = Post

class FotoSerializer(ModelSerializer):

	class Meta:
		model = Foto

#class BannerSerializer(ModelSerializer):
#
#	class Meta:
#		model = Post
#		fields = ('id','titulo')
