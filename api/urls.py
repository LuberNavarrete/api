from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from views import FotoViewSet,CategoriaViewSet,PostViewSet
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'fotos',FotoViewSet)
router.register(r'categorias',CategoriaViewSet)
router.register(r'posts',PostViewSet)

urlpatterns = [
	url(r'^',include(router.urls)),
	url(r'^logearse/', views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)