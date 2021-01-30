from django.urls import path
from .views import (
    ShortUrlCreateView,
    ShortUrlRedirectview,
)


urlpatterns = [
    path('create-short-url/', ShortUrlCreateView.as_view()), 
]
