from django.urls import path
from home.views import *

urlpatterns = [
    path('get-person/', get_persons),
    path('save-person/', save_person),
    # Other URL patterns...
]
