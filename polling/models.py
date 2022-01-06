# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Model definitions for polling app.
"""

from django.db import models


class Poll(models.Model):

    """
    Definition of the model for polls.
    """

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):

        return self.title
