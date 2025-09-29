from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone   # ✅ important for default datetime

LORRY_TYPES = [
    ('mini', 'Mini Truck (₹1000)'),
    ('medium', 'Medium Truck (₹2000)'),
    ('large', 'Large Truck (₹3000)'),
]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    date = models.DateField()
    lorry_type = models.CharField(max_length=20, choices=LORRY_TYPES, default='mini',null=True)
    price = models.IntegerField(default=1000)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(default=timezone.now)  # ✅ fixed

    def save(self, *args, **kwargs):
        prices = {'mini': 1000, 'medium': 2000, 'large': 3000}
        self.price = prices.get(self.lorry_type, 1000)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.pickup_location} to {self.drop_location} ({self.lorry_type})"
