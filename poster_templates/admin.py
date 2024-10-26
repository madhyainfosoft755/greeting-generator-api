from django.contrib import admin
from .models import Client, Festival, Template, Quotation     # Names of models

admin.site.register(Client)
admin.site.register(Festival)
admin.site.register(Template)
admin.site.register(Quotation)