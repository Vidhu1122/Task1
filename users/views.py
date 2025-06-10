from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def input_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, "Mobile number already exists.")
            return render(request, 'input.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'input.html')

        User.objects.create(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            password=password
        )
        return redirect('display')

    return render(request, 'input.html')

def display_view(request):
    users = User.objects.all()
    return render(request, 'display.html', {'users': users})
