from django.urls import path
from . views import local_news
urlpatterns = [
    path('bg/',local_news,name='local_news'),
]
