from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is success """
        email = "hakanyalcinkaya@gmail.com"
        password = "loremIpsumDolor"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name="Hakan",
            last_name="Yalcinkaya",
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """is user email address normalized?"""
        email = "hakanYALCINKAYA@gmail.com"
        password = "loremIpsumDolor"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if new user try not validated email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'Password'
            )

    def test_creating_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            email="staff@admin.com",
            password="Lorem12345"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)