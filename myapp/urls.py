from django.urls import path
from . import views
from .service import user_report_service

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("api/notifications/create/", views.notifications, name="notifications_create"),
    path("api/notifications/accepted/", views.accepted, name="accepted"),
    path(
        "api/MakeUserReportService/",
        lambda request: user_report_service.MakeUserReportService().execute(),
        name="MakeUserReportService",
    ),
]
# api / notifications / accepted
