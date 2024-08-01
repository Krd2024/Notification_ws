from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("api/notifications/create/", views.notifications, name="notifications_create"),
    path("api/notifications/accepted/", views.accepted, name="accepted"),
]
# api / notifications / accepted
