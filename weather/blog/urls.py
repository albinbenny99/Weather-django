from . import views
from django.urls import path

urlpatterns = [
  path('blogs/', views.PostList.as_view(), name="blog-list"),
  path('blogs/<slug:slug>/',  views.DetailView.as_view(), name="post_detail"),
]