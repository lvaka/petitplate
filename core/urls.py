"""Core URLS core.urls."""
from django.urls import re_path
from core.views import index

urlpatterns = [
    re_path(r'', index, name='index')
]
