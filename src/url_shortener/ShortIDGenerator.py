from django.conf import settings
from .models import Url
from random import choice
import string


class ShortIDGenerator:
    """
    Add in setting:
    BASE_SITE_URLL: str = 'http://your-site-name.com/'
    SHORT_URL_ID_LENGTH: int = num
    """
    def __init__(self):
        self.LENGTH = settings.SHORT_URL_ID_LENGTH
        self.chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    def gen_short_id(self) -> str:
        short_id = ''.join(choice(self.chars) for x in range(self.LENGTH))
        return short_id
    
    def __call__(self) -> str:
        while True:
            short_id = self.gen_short_id()
            try:
                temp = Url.objects.get(pk=short_id)
            except:
                return short_id
