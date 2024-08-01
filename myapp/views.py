from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Notification, User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password


def index(request):
    context = {}
    if request.user.is_authenticated:
        users_query = User.objects.all()
        notifications_query = Notification.objects.filter(
            recipient=request.user, is_read=False
        )
        context.update({"users": users_query, "notifications": notifications_query})
    return render(request, "myapp/index.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            username = username.lower()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.add_message(
                    request, messages.INFO, "НЕПРАВИЛЬНОЕ ИМЯ ПОЛЬЗОВАТЕЛЯ ИЛИ ПАРОЛЬ"
                )
                return redirect("login")
        except:
            messages.add_message(request, messages.INFO, "ОШИБКА!")
            return redirect("login")
    return render(request, "myapp/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            username = username.lower()
            password = make_password(password)
            user = User(username=username, password=password)
            user.save()
            return redirect("login")
        except:
            messages.add_message(request, messages.INFO, "ОШИБКА!")
            return redirect("register")

    return render(request, "myapp/register.html")


def notifications(request):
    """Отправить сигнал пользователю"""

    if request.method != "POST":
        return render(request, "myapp/404.html")

    print(request.POST, "<<<<< -------------")
    user = get_object_or_404(User, username=request.POST.get("username"))

    add_signal = Notification.objects.create(
        sender=request.user,
        recipient=user,
        notification_type="signal",
        related_object_id=1,
    )
    # print("Ok") if add_signal.exists() else print("Not ok")
    return redirect("home")


def accepted(request, **kwargs):
    print(request.GET.get("q"))
    return JsonResponse({"res": "Sdelano"})
    # return redirect("home")


# Create your views here.
