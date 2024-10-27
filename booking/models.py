from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # New field to track if booking is active

    def __str__(self):
        return f"{self.name} - {self.item.name}"
