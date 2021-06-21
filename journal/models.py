from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class Journal(models.Model):
    """Model for representing a journal"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="journals")
    name = models.CharField(_("Name of Journal"), max_length=50, help_text=_(
        "Enter the name you would like to give to your journal."), null=False, blank=False)
    description = models.TextField(_("Description"), max_length=100, help_text=_(
        "What is this journal about?"), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    background_color = models.CharField(max_length=10, help_text=_(
        "Color to give to the background of the journal"))
    text_color = models.CharField(
        max_length=10, help_text=_("color to give the text"))

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Journals"


class Entry(models.Model):
    """Model for representing a journal's entry"""
    journal = models.ForeignKey("journal.Journal", on_delete=models.CASCADE,
                                null=False, blank=False, related_name="entries")
    text = models.TextField(null=False, blank=False,
                            help_text=_("Pour out your heart here"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.journal} entry on {self.created}"


    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Entries"