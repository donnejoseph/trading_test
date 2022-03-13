from django.urls import path
from .views import SignalView

urlpatterns = [
    path('signal', SignalView.as_view(), name="signal"),
]
