from django.contrib import admin

from django.contrib import admin
from .models import JournalTag, JournalEntry


@admin.register(JournalTag)
class JournalTagAdmin(admin.ModelAdmin):
    pass


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    pass
