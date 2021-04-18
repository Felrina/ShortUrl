import random
import string
from django.conf import settings 

SHORTURL_MIN = getattr(settings, "SHORTURL_MIN", 6)

def code_generator(size=SHORTURL_MIN, chars=string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for i in range(size))

def create_shortcut(instance, size=SHORTURL_MIN):
    new_code = code_generator(size=size)
    urlmodel = instance.__class__
    print(instance)
    print(instance.__class__)
    query_exists = urlmodel.objects.filter(short_url=new_code).exists()
    if query_exists:
        return create_shortcut(size=size)
    return new_code