from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('mood_tracker_list/', mood_tracker_list, name='mood_tracker_list'),
    path('signup_view/',signup_view, name= 'signup'),
    path('login_view/',login_view, name= 'login'),
]