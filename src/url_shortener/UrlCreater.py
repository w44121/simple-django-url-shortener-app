from django.conf import settings
from .models import Url
from .ShortIDGenerator import ShortIDGenerator


class UrlCreater:
    def __init__(self, url: str):
        self.short_id = ShortIDGenerator()()
        self.url = url
        self.BASE_URL = settings.BASE_SITE_URL

    def __call__(self) -> Url:
        url = Url(httpurl=self.url, short_id=self.short_id)
        return url
