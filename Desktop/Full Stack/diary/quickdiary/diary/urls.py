from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('mood_tracker_list/', mood_tracker_list, name='mood_tracker_list'),
]