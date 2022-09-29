from django.urls import path
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from blogging.models import Post


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class PostFeed(Feed):
    title = "My Django Blog RSS Feed"
    description = "RSS feed for My Django Blog"

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return str(path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"))
