from django.shortcuts import render
from django.http import HttpResponse
from vpnSale import models
from django.contrib.auth.decorators import login_required
from accounts.models import profileModel
from accounts.functions import xui_login_func
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import accounts

# Create your views here.

def testView(request):
    context = {"1":"aa"}
    return render(request, "vpnSale/firstpage.html", context)

def index(request):

    locations_list = models.locationModel.objects.all()

    my_text = {
        "location_context" : locations_list
    }
    return render(request, "vpnSale/index.html", context = my_text)

def infoV2ray(request):
    my_text = {"text_for_page" : "hello for new world"}
    return render(request, "vpnSale/info-v2ray.html", context=my_text)

def howToUseV2ray(request):
    my_text = {"text_for_page" : "hello for new world"}
    return render(request, "vpnSale/how-to-use.html", context=my_text)

def serverLocationDetails(request, location_id):
    location = models.locationModel.objects.get(pk=location_id)
    context={
        "locationDetails" : location
    }
    return render(request, "vpnSale/server_location_details.html", context)

def serverList(request):
    server = models.serverModel.objects.all()
    context={
        "serverList" : server
    }
    return render(request, "vpnSale/server-list.html", context)

@login_required
def serverDetails(request, server_id):
    
    server_details = models.serverModel.objects.get(pk=server_id)
    context={
        "server__Details" : server_details
    }

    if request.method == "POST" and "get_vpn" in request.POST:
        email_request = request.user.email
        client_add = xui_login_func.add_client(email_request)
        return HttpResponseRedirect(reverse(accounts.views.profileView))
    return render(request, "vpnSale/server_details.html", context)