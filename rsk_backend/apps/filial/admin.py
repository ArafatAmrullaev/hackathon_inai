from django.contrib import admin

from .models import Address, Filial, Kassa

admin.site.register(Address)
admin.site.register(Filial)
admin.site.register(Kassa)