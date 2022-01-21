# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Django app configuration.
"""

from django.apps import AppConfig


class BloggingConfig(AppConfig):

    """
    Configuration for blogging app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blogging"
