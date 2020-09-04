from django.contrib import admin
from temperature.models import Temperature

# Register your models here.
class TemperatureAdmin(admin.ModelAdmin):
    model = Temperature
    list_display = ["uuid", "timestamp", "temperature", "duration"]

admin.site.register(Temperature, TemperatureAdmin)
