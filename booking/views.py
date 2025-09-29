from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import BookingForm,LoginForm
from .models import Booking
from django.contrib import messages
def home(request):
    return render(request, 'booking/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'booking/login.html', {"form": form})


def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out successfully.")
    return redirect('login') 

@login_required
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('mybookings')
    else:
        form = BookingForm()
    return render(request, 'booking/book.html', {"form": form})

@login_required
def mybookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/mybookings.html', {"bookings": bookings})
