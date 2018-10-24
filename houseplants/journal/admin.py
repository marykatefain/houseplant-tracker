from django.contrib import admin

from django.contrib import admin
from .models import JournalTag, JournalEntry


@admin.register(JournalTag)
class JournalTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('publish_date', 'plant')
