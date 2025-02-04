from django.contrib import admin
from django.contrib.gis import admin
from .models import Place

# Register your models here.
@admin.register(Place)
class ImportTrekAdmin(admin.GISModelAdmin):
    list_display = ('name', 'location', )



