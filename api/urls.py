from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter, SimpleRouter
from views import FotoViewSet,CategoriaViewSet,PostViewSet,BannerViewSet
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r'fotos',FotoViewSet)
router.register(r'categorias',CategoriaViewSet)
router.register(r'posts',PostViewSet)
##Vista para el banner
router.register(r'banner',BannerViewSet)

urlpatterns = [
	url(r'^',include(router.urls)),
	url(r'^logearse/', views.obtain_auth_token),
	url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)