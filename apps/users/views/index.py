from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')


def signin(request):
    return render(request, 'pages/signin.html')

def signup(request):
    return render(request, 'pages/signup.html')
