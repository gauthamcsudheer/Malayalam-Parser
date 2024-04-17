# parser_app/urls.py

from django.urls import path
from .views import home, parse_text

urlpatterns = [
    path('', home, name='home'),
    path('parse/', parse_text, name='parse_text'),
]
