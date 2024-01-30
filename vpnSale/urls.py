from django.urls import path
from vpnSale import views


urlpatterns = [
    path("v2ray-info", views.infoV2ray),
    path("how-to-use-v2ray", views.howToUseV2ray),
    path("server-location-details/<int:location_id>", views.serverLocationDetails),
    path("server-list", views.serverList),
    path("server-details/<int:server_id>", views.serverDetails),
]