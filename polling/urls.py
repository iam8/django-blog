# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
URL patterns for polling app.
"""

from django.urls import path
from polling.views import PollListView, PollDetailView


urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll_detail")
]
