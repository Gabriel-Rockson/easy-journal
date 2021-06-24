from django.db import models
from journal.models import Journal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Entry(models.Model):
    """Model for representing a journal's entry"""
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE,
                                null=False, blank=False, related_name="entries")
    text = models.TextField(null=False, blank=False,
                            help_text=_("Pour out your heart here"))
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.journal} entry on {self.created}"


    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Entries"
