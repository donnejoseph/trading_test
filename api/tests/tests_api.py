from rest_framework.test import APITestCase
from accounts.models import UserAccount, Profile
from api.trading_bot import TradingAPI
import os


class TradingApiTestCase(APITestCase):

    def test_get_account_info(self):
        user = UserAccount.objects.create(email="test@email.com", name="test")
        Profile.objects.create(user_account=user, exante_account_id=os.getenv('CLIENT_ID'), token=os.getenv('TOKEN'))

        trading_api = TradingAPI(user)

        response = trading_api.get_account_info()
        self.assertEqual(response.status_code, 200)

        response = trading_api.get_active_orders()
        self.assertEqual(response.status_code, 200)

        response = trading_api.get_historical_orders()
        self.assertEqual(response.status_code, 200)