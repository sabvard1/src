from django.urls import path
from accounts import views


urlpatterns = [
    path("login", views.loginView),
    path("logout", views.logoutView),
    path("signup", views.signupView),
    path("profile", views.profileView),

]