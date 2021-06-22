from django.http import request
from django.shortcuts import render
from .forms import JournalCreateForm
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class JournalCreateView(LoginRequiredMixin, CreateView):
    form_class = JournalCreateForm
    template_name = "journal/create-journal.html"
    success_url = reverse_lazy("user:user-profile")

    def form_valid(self, form):
        journal = form.save(commit=False)
        journal.user = self.request.user
        journal.save()
        return super().form_valid(form)