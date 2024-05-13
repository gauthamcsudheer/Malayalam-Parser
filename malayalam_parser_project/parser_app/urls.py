# parser_app/urls.py

from django.urls import path
from .views import home, parse_text
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('parse/', parse_text, name='parse_text'),
    path('explore/', views.explore, name='explore'),
    path('pos/<str:pos_tag>/', views.pos_tag_detail, name='pos_tag_detail'),
]
