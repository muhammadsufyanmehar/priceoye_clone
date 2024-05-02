from django.urls import re_path, include, path
from .views import simple_mail

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.social.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('mail', simple_mail),
    
]
