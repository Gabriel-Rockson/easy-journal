from django import forms
from django.forms import fields
from .models import Journal


class JournalCreateForm(forms.ModelForm):
    """Model form to handle creation of a new journal object"""

    class Meta:
        model = Journal
        fields = ["name", "description", "background_color", "text_color"]