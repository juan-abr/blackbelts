from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlackBelts

# Create your views here.
class BlackBeltsListView(ListView):
    model = BlackBelts

class BlackBeltsDetailView(DetailView):
    model = BlackBelts
    pk_url_kwarg = 'blackbelts_id'