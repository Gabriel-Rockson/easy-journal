from django.urls import path
from .views import JournalCreateView

app_name="journal"
urlpatterns = [
    path("create/", JournalCreateView.as_view(), name="create-journal")
]
