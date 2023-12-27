from django.contrib import admin
from .models import *

@admin.register(Korzina)
class AdminKorzina(admin.ModelAdmin):
    list_display = ('user', 'tovar', 'count', 'summa')
