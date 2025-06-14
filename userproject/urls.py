"""
URL configuration for userproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views   # ✅ Make sure you're importing from the app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.input_view, name='input'),
    path('display/', views.display_view, name='display'),
]



# This code defines the URL patterns for the Django project, linking the root URL to the input view and the 'display/' URL to the display view.
# The admin interface is also included for managing the application.
