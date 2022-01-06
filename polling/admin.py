# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Customization for polling site admin.
"""

from django.contrib import admin
from polling.models import Poll


# Registering the models
admin.site.register(Poll)
