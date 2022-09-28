from django.shortcuts import render
from django.template import loader
from django.urls import path
from django.contrib.syndication.views import Feed
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class LatestEntriesFeed(Feed):
    title = "My Django Blog RSS"
    link = "/posts/"
    description = "RSS feed for My Django Blog"

    def items(self):
        return Post.objects.order_by("-published_date")[:5]

    def item_title(self, item):
        return Post.title

    def item_description(self, item):
        return Post.text

    def item_link(self, item):
        return path("posts/<int:pk>/")
