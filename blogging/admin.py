# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Customization for site admin.
"""

from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):

    """
    Allows categories to be chosen for a post from the post admin page.
    """

    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):

    """
    Customize admin view of Category model.
    """

    exclude = ("posts",)


class PostAdmin(admin.ModelAdmin):

    """
    Customize admin view of Post model.
    """

    inlines = [
        CategoryInline,
    ]


# Registering the models
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
