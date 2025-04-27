from django.urls import path
from .views import search_imago_data, secret, throttle_check

urlpatterns = [
    path('imago-search/', search_imago_data, name='search_imago_data'),
    path('secret/', secret, name="secret"),
    path('throttle/', throttle_check, name="throttle_check"),
]