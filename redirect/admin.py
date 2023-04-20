from django.contrib import admin
# Signup.html your models here.
from .models import ShortenedLink
from .models import ShortLink
from .models import FullLink

admin.site.register(ShortenedLink)
admin.site.register(ShortLink)
admin.site.register(FullLink)
