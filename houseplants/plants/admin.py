from django.contrib import admin

from django.contrib import admin
from .models import Plant, Species


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass
