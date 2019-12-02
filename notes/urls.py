from django.conf.urls import url

from notes.views import NoteListView, NoteDetailView

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='note-list'),
    url(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
]