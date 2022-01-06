from django.urls import path
# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

from blogging.views import list_view, detail_view


urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail")
]
