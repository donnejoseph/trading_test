from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from api.serializers import SignalSerializer
from api.trading_bot import TradingAPI


class SignalView(ListCreateAPIView):
    """View that receive signal
    from TradingView,for sale or buy,
    according to RSI strategy"""
    serializer_class = SignalSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user
        data = self.request.data
        trading_api = TradingAPI(user)
        response = trading_api.place_order(data['side'], data['symbol'])
        if response.status_code == 201:
            trading_api.save_to_db(data, response)
        return Response(response.json(), status=response.status_code)
