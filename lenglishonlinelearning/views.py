from django.conf import settings
from django.shortcuts import render, redirect


def error_404_view(request, exception):
    """Error Handler 404 - Page Not Found"""
    return render(request, "not_found.html")


def error_500_view(request):
    """Error Handler 500 - Internal Server Error"""
    return render(request, "not_found.html")


def error_403_view(request):
    """Error Handler 403 - Page Not Found"""
    return render(request, "403.html")
