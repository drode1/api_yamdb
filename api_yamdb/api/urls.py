from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('v1/redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'
         ),
]
