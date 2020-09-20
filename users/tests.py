from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test", email="test@mail.com", password="testtest"
        )

        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@mail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="supertest", email="supertest@mail.com",
            password="supertest"
        )

        self.assertEqual(user.username, "supertest")
        self.assertEqual(user.email, "supertest@mail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
