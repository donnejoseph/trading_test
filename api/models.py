from django.db import models
from django.utils.timezone import now
from accounts.models import UserAccount


class Signal(models.Model):
    date = models.DateTimeField(default=now)
    side = models.CharField(max_length=5)
    symbol = models.CharField(max_length=10)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)


class Order(models.Model):
    bot = models.BooleanField(default=True)
    date = models.DateTimeField(default=now)
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
