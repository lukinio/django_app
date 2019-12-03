from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Note
from .forms import NoteCreateForm, NoteUpdateForm


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
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'notes/note_update_form.html'
    form_class = NoteUpdateForm

    def test_func(self):
        return self.request.is_superuser or self.object.created_by == self.request.user

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Note, pk=pk_)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)