from django.contrib import admin
from .models import Estado, Cidade, Pessoa

admin.site.register(Estado)
admin.site.register(Pessoa)
admin.site.register(Cidade)