from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # other apps paths
    path('', include('home.urls', namespace="home")),
    path('user/', include('users.urls', namespace="user")),
    path('journals/', include('journal.urls', namespace="journal")),
    path('entries/', include("entry.urls", namespace="entry")),
]
