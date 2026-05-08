from django.contrib import admin

# Register your models here.

#permet de gérer les PDF depuis l’interface Django admin
from .models import Document

admin.site.register(Document)