from django import forms
from django.forms import fields

from .models import Entry


class EntryCreateUpdateForm(forms.ModelForm):
    """Form to create and / or update a journal entry"""

    class Meta:
        model = Entry  
        fields = ["text"]
