import requests

from accounts.models import Profile
from api.models import Signal, Order


class TradingAPI:
    """Demo Bot for trading in https://exante.eu/"""

    base_url = 'https://api-demo.exante.eu/'

    def __init__(self, user):
        self.user = user
        self.profile = Profile.objects.get(user_account=self.user)
        self.headers = {'Authorization': 'Bearer ' + self.profile.token}

    def get_account_info(self):
        """ Return account info from exante.eu """

        url = self.base_url + 'md/3.0/accounts'
        response = requests.get(url, headers=self.headers)
        return response

    def place_order(self, side, symbol):
        """ Place new config order """
        data = {
            "duration": "immediate_or_cancel",
            "orderType": "market",
            "quantity": "100",
            "side": side,
            "symbolId": symbol,
            "accountId": self.profile.exante_account_id
        }

        url = self.base_url + "trade/3.0/orders"
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def get_active_orders(self):
        """ Return active orders from exante.eu """
        url = self.base_url + "trade/3.0/orders/active"
        response = requests.get(url, headers=self.headers)
        return response

    def get_historical_orders(self):
        """ Return orders history from exante.eu """
        url = self.base_url + "trade/3.0/orders"
        response = requests.get(url, headers=self.headers)
        return response

    def save_to_db(self, data, response):
        """Saved to db Orders and Signals"""
        signal = Signal.objects.create(side=data['side'], symbol=data['symbol'], user=self.user)
        order_id = response.json()[0]["orderId"]
        Order.objects.create(signal=signal, order_id=order_id)
