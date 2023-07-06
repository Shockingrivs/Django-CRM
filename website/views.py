from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home(request):
    # Check if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has ingresado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Hubo un error ingresando. Por favor, inténtalo de nuevo.")
            return redirect('home')
    else:
        return render(request, 'home.html')



def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado la sesión")
    return redirect('home')


def register_user(request):
    return render(request,'register.html', {})
