from rest_framework.test import APITestCase
from accounts.models import UserAccount


class CreateSuperUserTestCase(APITestCase):
    def setUp(self):
        UserAccount.objects.create_superuser('test@email.com', 'test', 'password')

    def test_create_superuser(self):
        user = UserAccount.objects.get(name='test')
        self.assertEqual(user.get_full_name(), "test")
        self.assertEqual(user.get_short_name(), "test")
        self.assertEqual(str(user), "test@email.com")
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)


class CreateUserTestCase(APITestCase):
    def setUp(self):
        UserAccount.objects.create_user('test@email.com', 'test', 'pass')

    def test_create_user(self):
        user = UserAccount.objects.get(name='test')
        self.assertEqual(user.get_full_name(), "test")
        self.assertEqual(user.get_short_name(), "test")
        self.assertEqual(str(user), "test@email.com")
        self.assertEqual(user.is_staff, False)


class RiseErrorTestCase(APITestCase):

    def test_check_user_email(self):
        with self.assertRaises(ValueError):
            UserAccount.objects.create_user('', 'test', 'pass')
