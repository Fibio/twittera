from django.urls import path

from .views import get_stats

urlpatterns = [
    path('^$', get_stats),
]
