from django.test import TestCase
from accounts.models import UserAccount
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class TestCaseBase(TestCase):
    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = UserAccount.objects.create(email="test@email.com", name="test")

        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class CreateProfileTestCase(TestCaseBase):
    url = reverse("profile")

    def test_create_profile(self):
        data = {
            "exante_account_id": "PWM0000.000",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
        response = self.client.post(self.url, data, **self.bearer_token)
        self.assertEqual(response.status_code, 201)

    def test_create_profile_without_data(self):
        data = {"exante_account_id": "PWM0000.000"}
        response = self.client.post(self.url, data, **self.bearer_token)
        self.assertEqual(response.status_code, 400)
