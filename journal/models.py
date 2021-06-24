from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Journal(models.Model):
    """Model for representing a journal"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="journals")
    name = models.CharField(_("Name of Journal"), max_length=50, help_text=_(
        "Enter the name you would like to give to your journal."), null=False, blank=False)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = models.TextField(_("Description"), max_length=100, help_text=_(
        "What is this journal about?"), null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    background_color = models.CharField(_("Background Color"), max_length=10, help_text=_(
        "Color to give to the background of the journal"))
    text_color = models.CharField(_("Text Color"),
        max_length=10, help_text=_("color to give the text"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("journal:journal-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.created}")
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Journals"

