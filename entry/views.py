from django.shortcuts import render
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
# TODO 
"""
todo - add create view
todo - add get entry view
todo - add update entry view
todo - add delete entry view 
todo - add get all entries view
"""

class EntryCreateView(LoginRequiredMixin, CreateView):
    """View to create a new journal entry"""