from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from blog.models import BlogPost
from .forms import CommentForm


# Create your views here.

class IndexPageView(ListView):
    template_name = "blog/index.html"
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllBlogPostView(ListView):
    template_name = "blog/all-posts.html"
    model = BlogPost
    context_object_name = "posts"


class BlogPostDetailView(View):

    def is_stored_post(self, request, post_id):
        stored_post = request.session.get("stored_posts")
        if stored_post is not None:
            is_saved_for_later = post_id in stored_post
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = BlogPost.objects.get(slug=slug)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),
            "saved_for_later": self.is_stored_post(request, post.id)
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = BlogPost.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),
            "saved_for_later": self.is_stored_post(request, post.id)
        })


class ReadLaterView(View):

    def get(self, request):
        stored_post = request.session.get("stored_posts")
        context = {}
        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_post"] = False
        else:
            posts = BlogPost.objects.filter(id__in=stored_post)
            context["posts"] = posts
            context["has_post"] = True

        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_post = request.session.get("stored_posts")

        if stored_post is None:
            stored_post = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)

        request.session["stored_posts"] = stored_post

        return HttpResponseRedirect("/")
