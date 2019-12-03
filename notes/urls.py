from django.conf.urls import url
from django.urls import path
from notes import views

app_name='notes'
urlpatterns = [
    path('', views.NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('add/', views.NoteCreateView.as_view(), name='note-add'),
]