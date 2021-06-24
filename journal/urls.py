from django.urls import path
from .views import JournalCreateView, JournalDeleteView, JournalDetailView, JournalListView, JournalUpdateView

app_name="journal"
urlpatterns = [
    path("", JournalListView.as_view(), name="list-journals"),
    path("create/", JournalCreateView.as_view(), name="create-journal"),
    path("update/<slug:slug>/", JournalUpdateView.as_view(), name="update-journal"),
    path("delete/<slug:slug>/", JournalDeleteView.as_view(), name="delete-journal"),
    path("<slug:slug>/", JournalDetailView.as_view(), name="journal-detail"),
]
