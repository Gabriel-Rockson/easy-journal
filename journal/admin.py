from django.contrib import admin
from journal.models import Journal, Entry


class EntryInline(admin.TabularInline):
    model = Entry


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
    list_display = ["name", "created"]

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["journal", "created"]