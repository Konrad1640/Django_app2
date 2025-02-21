import os
from django.core.wsgi import get_wsgi_application
from django.db import models
from django.contrib.auth.models import User

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    class Meta:
        app_label = 'restauracja'

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.date}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow NULL and blank values
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(default='No comment provided')

    def __str__(self):
        return f"{self.user.username} - {self.dish.name}" if self.user else f"Anonymous - {self.dish.name}"
