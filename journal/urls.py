from django.urls import path
from .views import JournalCreateView, JournalDetailView, JournalListView

app_name="journal"
urlpatterns = [
    path("", JournalListView.as_view(), name="list-journals"),
    path("create/", JournalCreateView.as_view(), name="create-journal"),
    path("<slug:slug>/", JournalDetailView.as_view(), name="journal-detail"),
]
