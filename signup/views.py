from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.


def register(request):

    # Your code to handle the registration process goes here.
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conformpassword = request.POST['conformpassword']

        # Check if any of the fields are empty
        if not username or not email or not password or not conformpassword:
            messages.info(request, "Please fill all the fields!")
            return redirect('register')


        # Validate the form inputs.
        if password == conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, "Registration successful!")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match!")
            return redirect('register')
 
    # Save the user data to your database or any other storage system.
    else:
        return render(request, 'register.html')

def login_view(request):

    # Your code to handle the login process goes here.
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']


        # Check if any of the fields are empty
        if not username or not password:
            messages.info(request, "Please fill all the fields!")
            return redirect('login')

        # Validate the form inputs.
        user = authenticate(username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
        
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')