from django.contrib import admin

from home.views import add
from .models import Info

# Register your models here.
admin.site.register(Info)