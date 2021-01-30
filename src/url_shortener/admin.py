from django.contrib import admin
from .models import Url


models = [Url, ]

admin.site.register(models)
