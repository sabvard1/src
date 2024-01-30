from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import vpnSale.views
import accounts
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileRegisterForm
from django.contrib.auth.models import User
from accounts.models import profileModel
from .functions import xui_login_func
from vpnSale.models import serverModel


from django.contrib import messages

# Create your views here.


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(reverse(accounts.views.profileView))
        else:
            context = {
                "username": username,
                "errorMessage": "USERNAME or PASSWORD is wrong!",
            }
            return render(request, "accounts/login.html", context)
    else:
        return render(request, "accounts/login.html", {})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(vpnSale.views.index))


def signupView(request):
    if request.method == "POST":
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)

        if profileRegisterForm.is_valid():
            user = User.objects.create_user(
                username=profileRegisterForm.cleaned_data["username"],
                email=profileRegisterForm.cleaned_data["email"],
                password=profileRegisterForm.cleaned_data["password"],
                first_name=profileRegisterForm.cleaned_data["first_name"],
                last_name=profileRegisterForm.cleaned_data["last_name"],
            )
            user.save()

            profileModel1 = profileModel(
                user=user,
                ProfileImage=profileRegisterForm.cleaned_data["ProfileImage"],
                Gender=profileRegisterForm.cleaned_data["Gender"],
            )

            profileModel1.save()

            return HttpResponseRedirect(reverse(vpnSale.views.index))
        else:
            context = {
                "error_message": profileRegisterForm.errors,
                "formData": profileRegisterForm,
            }

            return render(request, "accounts/signup.html", context)
    else:
        profileRegisterForm = ProfileRegisterForm()

    context = {"formData": profileRegisterForm}

    return render(request, "accounts/signup.html", context)


@login_required
def profileView(request):
    email_request = request.user.email


    client_details_request = xui_login_func.get_clinet_data(email_request).json()
    if client_details_request["success"] == True:
        if client_details_request["obj"] == None:
            client_details = {"status": "No accounts yet"}
            config_gen_result = ""
        else:
            client_details = {"status": "Account is active"}
            inbound_details = xui_login_func.get_inbound_data("1", email_request)
            config_gen_result = xui_login_func.config_gen(
                inbound_details["raw_data"],
                inbound_details["user_id"],
                inbound_details["str_to_json_streamSettings"],
                email_request,
            )
    else:
        client_details = {"status": "Connection refused"}

    profile = request.user.profile

    context = {
        "profile": profile,
        "client_details": client_details,
        "client_config_result": config_gen_result,
    }

    return render(request, "accounts/profile.html", context)
