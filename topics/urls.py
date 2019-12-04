from django.urls import path
from topics import views

app_name='topics'
urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic-list'),
    path('<int:pk>', views.TopicDetailView.as_view(), name='topic-detail'),
    path('add/', views.TopicCreateView.as_view(), name='topic-add'),
    path('<int:pk>/update/', views.TopicUpdateView.as_view(), name='topic-update'),
    path('<int:pk>/delete/', views.TopicDeleteView.as_view(), name='topic-delete'),
]