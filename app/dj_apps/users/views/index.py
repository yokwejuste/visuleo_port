from django.shortcuts import render


def index(request):
    return render(request, "pages/index.html")


def signin(request):
    return render(request, "pages/signin.html")


def signup(request):
    return render(request, "pages/signup.html")


def visu_404(request, exception):
    return render(request, "pages/404.html", status=404)
