from django.shortcuts import render
from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = "users/profile.html"
