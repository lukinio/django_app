from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('create/', views.CreateNote.as_view(), name='create-note'),
]