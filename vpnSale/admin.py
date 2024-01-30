from django.contrib import admin
from vpnSale.models import locationModel, serverModel, configModel, profileModel

# Register your models here.

admin.site.register(locationModel)
admin.site.register(serverModel)
admin.site.register(configModel)
