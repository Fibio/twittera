from django.urls import re_path
from django.views.generic import TemplateView

from .views import TweetsCountView

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="main.html"), name="main"),
    re_path(r'^counts/$', TweetsCountView.as_view(), name='tweets-count'),
]
