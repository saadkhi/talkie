"""
URL configuration for talkie project.

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

from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("plan/<int:plan_id>/", views.plan_details, name="plan_details"),
    path("download/<int:plan_id>/", views.download_plan, name="download_plan"),     # <-- Add this line
    path("plan_available/", views.plan_available, name="plan_available"),
    path("plan_store/", views.plan_store, name="plan_store"),

    

    path("reload/", include("django_browser_reload.urls")),  # For live reloading
]