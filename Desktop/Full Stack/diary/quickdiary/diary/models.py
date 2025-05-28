from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MoodTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user account
    date = models.DateField(auto_now_add=True)  # Auto-set date of entry
    time = models.TimeField(auto_now_add=True)  # Auto-set time of entry
    mood = models.CharField(max_length=50)  # Mood description (e.g., Happy, Sad)
    mood_intensity = models.IntegerField()  # Mood intensity (1-10)
    performance = models.CharField(max_length=50)  # Performance description (e.g., Excellent, Good)
    performance_score = models.IntegerField(null=True, blank=True)  # Optional performance score (1-10)
    stress_level = models.CharField(max_length=50)  # Stress level (Low, Moderate, High)
    energy_level = models.CharField(max_length=50)  # Energy level (Low, Medium, High)
    physical_health = models.TextField(null=True, blank=True)  # Health details (e.g., Sleep, Diet)
    activities = models.TextField(null=True, blank=True)  # List of activities influencing mood
    social_interaction = models.TextField(null=True, blank=True)  # Quality of social interactions
    weather = models.CharField(max_length=50, null=True, blank=True)  # Weather conditions (Sunny, Rainy)
    mental_clarity = models.CharField(max_length=50, null=True, blank=True)  # Focused or distracted
    gratitude_notes = models.TextField(null=True, blank=True)  # Gratitude or positive notes
    self_care = models.TextField(null=True, blank=True)  # Self-care activities

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.mood}"