from django import forms
from notes.models import Note


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'title', 'body']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'title', 'body']

class NoteDeleteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"