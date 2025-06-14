from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re

def input_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        mobile_number = request.POST.get('mobile_number', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # --- VALIDATIONS ---
        if not re.match(r'^[A-Za-z ]+$', full_name):
            messages.error(request, "Name should contain only letters and spaces.")
            return render(request, 'input.html')

        if not re.match(r'^\d{10}$', mobile_number):
            messages.error(request, "Mobile number must be exactly 10 digits.")
            return render(request, 'input.html')

        if User.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, "This mobile number is already registered.")
            return render(request, 'input.html')

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, "Enter a valid email address.")
            return render(request, 'input.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'input.html')

        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$', password):
            messages.error(request, "Password must be at least 8 characters, include 1 uppercase letter, 1 digit, and 1 special character.")
            return render(request, 'input.html')

        # --- SAVE TO DATABASE ---
        User.objects.create(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            password=password  # (Plaintext not recommended – use hashing in real apps)
        )

        return redirect('display')  # assuming your display page URL name is 'display'

    return render(request, 'input.html')


def display_view(request):
    users = User.objects.all()
    return render(request, 'display.html', {'users': users})
# This code defines two views for a Django application: one for inputting user data with validation and another for displaying all registered users.
# It includes form validation for name, mobile number, email, and password, and handles errors with messages.
# The input view saves valid user data to the database and redirects to the display view, which lists all users.s