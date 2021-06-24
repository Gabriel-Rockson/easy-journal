from django import forms
from django.forms import fields
from .models import Journal


class JournalCreateUpdateForm(forms.ModelForm):
    """Model to create or update a journal object"""

    class Meta:
        model = Journal
        fields = ["name", "description", "background_color", "text_color"]