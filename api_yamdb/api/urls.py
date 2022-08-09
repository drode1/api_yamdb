from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='category')
router_v1.register(r'genres', GenreViewSet, basename='genre')
router_v1.register(r'titles', TitleViewSet, basename='title')

v1_urlpatterns = (
    [
        path('redoc/', TemplateView.as_view(template_name='redoc.html'),
             name='redoc'
             ),
        path('', include(router_v1.urls)),
    ],
    'v1'
)

urlpatterns = [
    path('v1/', include(v1_urlpatterns))
]
