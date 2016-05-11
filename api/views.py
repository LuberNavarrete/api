from serializers import CategoriaSerializer,PostSerializer,FotoSerializer,BannerSerializer
from models import Categoria, Post, Foto
from rest_framework import viewsets,permissions,filters
from rest_framework.pagination import PageNumberPagination

##Remueve tags de html
from django.utils.html import strip_tags

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class FotoViewSet(viewsets.ModelViewSet):
	serializer_class = FotoSerializer
	queryset = Foto.objects.all()
	# lookup_field = 'post'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		query = self.request.query_params
		queryset = self.queryset
		if 'post' in query.keys():
			queryset = queryset.filter(post = query.get('post'))
		return queryset

class CategoriaViewSet(viewsets.ModelViewSet):
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all()
	lookup_field = 'id'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	pagination_class = StandardResultsSetPagination
	
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
	lookup_field = 'slug'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	pagination_class = StandardResultsSetPagination

	def get_queryset(self):
		query = self.request.query_params
		queryset = self.queryset
		if 'posteable' in query.keys():
			pos = True if query.get('posteable') == 'true' else False
			queryset = queryset.filter(posteable = pos)
		if 'categoria' in query.keys():
			queryset = queryset.filter(categoria__titulo = query.get('categoria'))
		return queryset

class BannerViewSet(viewsets.ModelViewSet):
	serializer_class = BannerSerializer
	queryset = Post.objects.all().order_by('-posteado')[:3]
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)