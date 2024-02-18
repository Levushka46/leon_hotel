from django.contrib import admin
from .models import User, City, Hotel

# Register your models here.
admin.site.register(City)
admin.site.register(Hotel)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name")
    search_fields = ("first_name", "last_name", "email", "id")
