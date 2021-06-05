from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name="starting-page"),
    path('posts/', views.AllBlogPostView.as_view(), name="posts-page"),
    path('posts/<slug:slug>', views.BlogPostDetailView.as_view(), name="post-detail-page"),
    path('read-later', views.ReadLaterView.as_view(), name="read-later")
]
