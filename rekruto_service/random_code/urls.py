from random import random
from django.urls import path

from .views import random_code_view

urlpatterns = [
    path('', random_code_view),
]
