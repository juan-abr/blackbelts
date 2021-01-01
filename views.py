from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlackBelt

# Create your views here.
class BlackBeltListView(ListView):
    model = BlackBelt

class BlackBeltDetailView(DetailView):
    model = BlackBelt
    pk_url_kwarg = 'blackbelt_id'