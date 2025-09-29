from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'pickup_location', 'drop_location', 'date', 'status')

admin.site.register(Booking, BookingAdmin)
    