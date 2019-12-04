from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from notes.models import Note
from topics.models import Topic
from topics.forms import TopicCreateForm, TopicUpdateForm, TopicDeleteForm


class TopicListView(ListView):
    model = Topic
    queryset = Topic.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(is_public=True)
        return context

class TopicDetailView(DetailView):
    template_name = 'topics/topic_detail.html'
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    template_name = 'topics/topic_add_form.html'
    form_class = TopicCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('topics:topic-list')


class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'topics/topic_update_form.html'
    form_class = TopicUpdateForm

    def test_func(self):
        return self.request.user == self.get_object().created_by

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Topic, pk=pk_)

    def form_valid(self, form):
        form.instance.parent = self.get_object().parent
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('topics:topic-list')

class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    form_class = TopicDeleteForm

    def test_func(self):
        return self.request.user.is_superuser or self.object.created_by == self.request.user

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Topic, pk=pk_)

    def get_success_url(self):
        return reverse_lazy('topics:topic-list')