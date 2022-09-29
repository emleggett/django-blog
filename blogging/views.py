from django.urls import reverse
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
    link = "/feed/"
    description = "RSS feed for My Django Blog"

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )[:5]

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return post.text

    def item_link(self, post):
        return reverse("blog_detail", args=[post.pk])
