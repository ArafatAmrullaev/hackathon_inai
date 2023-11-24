from django.contrib import admin

from .models import Operation, Ticket

admin.site.register(Operation)
admin.site.register(Ticket)