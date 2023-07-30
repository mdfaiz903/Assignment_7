from django.urls import path
from . views import django_with_ai
urlpatterns = [
    path('dj/',django_with_ai,name='django_with_ai'),
]
