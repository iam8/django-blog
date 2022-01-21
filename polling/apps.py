# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Django polling app configuration.
"""

from django.apps import AppConfig


class PollingConfig(AppConfig):

    """
    Configuration for polling app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "polling"
