from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token

# Register your models here.
admin.site.register(Rahbarlar)
admin.site.register(Ishlar)
admin.site.register(Ariza)
admin.site.register(New)
admin.site.register(Hududlar)
admin.site.register(BaholashMezon)

# admin.site.register(Token)

