from django.urls import path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api.views import (UserViewSet, RegisterUser,
                       ObtainUserToken)

router_v1 = DefaultRouter()
router_v1.register('v1/users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
    path('v1/auth/signup/', RegisterUser.as_view(), name='user-signup'),
    path('v1/auth/token/', ObtainUserToken.as_view(), name='user-token'),
]

urlpatterns += router_v1.urls
