from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# from .models import
# from .forms import


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

