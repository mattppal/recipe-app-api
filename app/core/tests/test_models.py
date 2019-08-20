"""model testing notebook"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """functions to test our models"""
    def test_create_user_with_email_successful(self):
        """Test creating new user w/ email is successful"""
        email = 'test@ppal.me'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is not case-sensitive"""
        email = 'test@PPAL.ME'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test that a user cannot be created without a new email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@ppal.me',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
