from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    pass


@admin.register(Amenity)
class AmenitiesAdmin(admin.ModelAdmin):
    pass
