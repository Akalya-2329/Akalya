from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('mood_tracker_list/', mood_tracker_list, name='mood_tracker_list'),
    path('signup_view/',signup_view, name= 'signup'),
    path('login_view/',login_view, name= 'login'),
    path('edit_moodtracker/<int:pk>/', edit_moodtracker, name='edit_moodtracker'),
    path('delete_moodtracker/<int:pk',delete_moodtracker, name='delete_moodtracker')
]



    
