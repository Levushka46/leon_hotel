from django.contrib import admin
from .models import User, City, Hotel

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name")
    search_fields = ("first_name", "last_name", "email", "id")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)    

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "city")
    search_fields = ("name",)    