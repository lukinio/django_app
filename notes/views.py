from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Note
from .forms import NoteCreateForm


class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notes/note_add_form.html'
    form_class = NoteCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
