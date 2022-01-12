# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Code for the views for the blogging app.
"""

from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post

# CLASS-BASED VIEWS --------------------------------------------------------------------------------

class BlogListView(ListView):

    """
    List view class for blogging app.
    """

    template_name = "blogging/list.html"


class BlogDetailView(DetailView):

    """
    Detail view class for blogging app.
    """

    template_name = "blogging/detail.html"

    # No POST method required for blog post details (unlike poll detail).

#---------------------------------------------------------------------------------------------------


# FUNCTION-BASED VIEWS (OLD) -----------------------------------------------------------------------

def list_view(request):

    """
    List view of posts for the blogging app. Only published posts will be listed.
    """

    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}

    return render(request, "blogging/list.html", context)


def detail_view(request, post_id):

    """
    Detail view of posts for the blogging app. Only published posts will have this view.
    """

    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist as err:
        raise Http404 from err

    context = {"post": post}

    return render(request, "blogging/detail.html", context)

#---------------------------------------------------------------------------------------------------
