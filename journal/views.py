from journal.models import Journal
from django.http import request
from django.shortcuts import render
from .forms import JournalCreateForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class JournalCreateView(LoginRequiredMixin, CreateView):
    """View to create a new journal object"""
    form_class = JournalCreateForm
    template_name = "journal/create-journal.html"
    success_url = reverse_lazy("journal:list-journals")

    def form_valid(self, form):
        journal = form.save(commit=False)
        journal.user = self.request.user
        journal.save()
        return super().form_valid(form)


class JournalListView(LoginRequiredMixin, ListView):
    """View to list all journals"""
    template_name = "journal/list-journals.html"
    model = Journal
    context_object_name = "journals"


class JournalDetailView(LoginRequiredMixin, DetailView):
    """View to show the detail of a particular journal"""
    template_name = "journal/journal-detail.html"
    model = Journal
    context_object_name = "journal"