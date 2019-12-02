from django.conf.urls import url

from notes.views import NoteListView

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='note-list'),
]