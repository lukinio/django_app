from django import forms
from django.urls import reverse_lazy
from notes.models import Note


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

class NoteDeleteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"