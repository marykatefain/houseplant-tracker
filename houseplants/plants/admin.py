from django.contrib import admin

from django.contrib import admin
from .models import Plant, Species


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'species', 'location')


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('scientific_name', 'common_name')
