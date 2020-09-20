from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        test_user = User.objects.create_user(
            username="test", email="test@mail.com", password="testtest"
        )
        test_user.save()

        test_post = Post.objects.create(
            author=test_user, title="Test Title", link="testlink.com", upvotes=0
        )
        test_post.save()

    def test_title_post(self):
        post = Post.objects.get(id=1)
        expected_post_title = f"{post.title}"
        self.assertEqual(expected_post_title, "Test Title")

    def test_link_post(self):
        post = Post.objects.get(id=1)
        expected_post_link = f"{post.link}"
        self.assertEqual(expected_post_link, "testlink.com")
