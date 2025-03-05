from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_succesful(self):
        """ > Probar la creación de un nuevo usuario con un email, de manera correcta """
        email = 'test@gmail.com'
        username = 'test'
        password = 'test_123'
        user = get_user_model().objects.create_user(name = username, email = email, password = password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.COM'
        password = 'test_123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ > Probar error de creación de usuario con email invalido """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, None, '123')

    def test_create_new_super_user(self):
        """ > Probar super-usuario creado """
        user = get_user_model().objects.create_superuser('admin', 'admin@gmail.com', 'admin_1234567890')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)