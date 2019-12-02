from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from notes.models import Note


class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body', 'created_by']
