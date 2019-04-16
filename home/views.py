from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def index(request):
    """ A view that renders the index page """
    return render(request, "index.html")