from django import forms
from topics.models import Topic

class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'parent']

class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class TopicDeleteForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"