from django.urls import path
from .views import *

urlpatterns = [
    path('', BlackBeltListView.as_view(), name='black_belt_list_view'),
    path('<int:blackbelt_id>', BlackBeltDetailView.as_view(), name='black_belt_detail_view'),
]