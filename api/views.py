from serializers import CategoriaSerializer,PostSerializer,FotoSerializer
from models import Categoria, Post, Foto
from rest_framework import viewsets, permissions, filters

class FotoViewSet(viewsets.ModelViewSet):
	serializer_class = FotoSerializer
	queryset = Foto.objects.all()
	lookup_field = 'post'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoriaViewSet(viewsets.ModelViewSet):
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all()
	lookup_field = 'id'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_queryset(self):
		query = self.request.query_params
		queryset = self.queryset
		if 'titulo' in query.keys():
			queryset = queryset.filter(titulo = query.get('titulo'))
		if 'activo' in query.keys():
			act = True if query.get('activo') == 'true' else False
			queryset = queryset.filter(activo=act)
		return queryset

class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	queryset = Post.objects.all().order_by('-posteado')
	lookup_field = 'id'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		query = self.request.query_params
		queryset = self.queryset
		if 'posteable' in query.keys():
			pos = True if query.get('posteable') == 'true' else False
			queryset = queryset.filter(posteable = pos)
		if 'categoria' in query.keys():
			queryset = queryset.filter(categoria__titulo = query.get('categoria'))
		return queryset