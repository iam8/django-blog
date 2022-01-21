# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Unit tests for blogging app.
"""

import datetime

from django.utils.timezone import utc
from django.test import TestCase
from django.contrib.auth.models import User

from blogging.models import Post, Category


class FrontEndTestCase(TestCase):

    """
    Test the views provided in the front-end.
    """

    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):

        """
        Set-up for unit tests.
        """

        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)

        for count in range(1, 11):
            post = Post(title=f"Post {count} Title", text="foo", author=author)

            if count < 6:

                # Publish the first 5 posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate

            post.save()

    def test_list_only_published(self):

        """
        Test that only published posts are listed.
        """

        resp = self.client.get("/")

        # The content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("My Cool Blog Posts" in resp_text)

        for count in range(1, 11):
            title = f"Post {count} Title"

            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):

        """
        Test that only the detail pages of published posts can be visited.
        """

        for count in range(1, 11):
            title = f"Post {count} Title"
            post = Post.objects.get(title=title)
            resp = self.client.get(f"/posts/{post.pk}/")

            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)


class PostTestCase(TestCase):

    """
    Test the Post model.
    """

    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self) -> None:

        """
        Set-up for unit tests.
        """

        self.user = User.objects.get(pk=1)

    def test_string_representation(self):

        """
        Test the string representation of a Post instance.
        """

        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    """
    Test the Category model.
    """

    def test_string_representation(self):

        """
        Test the string representation of a Category instance.
        """

        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)
