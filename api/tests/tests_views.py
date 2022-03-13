from accounts.models import Profile
from django.test import TestCase
from accounts.models import UserAccount
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
import os


class TestCaseBase(TestCase):
    @property
    def bearer_token(self):
        user = UserAccount.objects.create(email="test@email.com", name="test")
        Profile.objects.create(user_account=user, exante_account_id=os.getenv('CLIENT_ID'), token=os.getenv('TOKEN'))
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class SignalTestCase(TestCaseBase):
    url = reverse("signal")

    def test_signal(self):
        data = {"side": "buy", "symbol": "ETH.USD"}
        response = self.client.post(self.url, data, **self.bearer_token)

        self.assertEqual(response.status_code, 201)
