from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, ReviewViewSet
from .views import (CategoryViewSet, GenreViewSet, ObtainUserToken,
                    RegisterUser, TitleViewSet, UserViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register(r'categories', CategoryViewSet, basename='category')
router_v1.register(r'genres', GenreViewSet, basename='genre')
router_v1.register(r'titles', TitleViewSet, basename='title')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

# Создаем отдельный кортеж для api урлов 1 версии
v1_urlpatterns = (
    [
        path('auth/signup/', RegisterUser.as_view(), name='user-signup'),
        path('auth/token/', ObtainUserToken.as_view(), name='user-token'),
        path('redoc/', TemplateView.as_view(template_name='redoc.html'),
             name='redoc'),
        path('', include(router_v1.urls)),

    ],
    'v1'
)

urlpatterns = [
    path('v1/', include(v1_urlpatterns)),
]
