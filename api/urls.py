from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from views import FotoViewSet,CategoriaViewSet,PostViewSet#,BannerViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'foto',FotoViewSet)
router.register(r'categoria',CategoriaViewSet)
router.register(r'post',PostViewSet)
#router.register(r'banner',BannerViewSet)

urlpatterns = patterns('api.views',
	url(r'^',include(router.urls)),
	url(r'^logearse/', views.obtain_auth_token),
)