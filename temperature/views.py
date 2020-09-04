from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from temperature.models import Temperature

import logging

db_logger = logging.getLogger('db')

# Create your views here.
class TemperatureView(View):
    
    def get(self, request, *args, **kwargs):
        temperatures = Temperature.objects.all()
        
        # On each GET request, logging the data was requested in the database.
        # Customize the django-db-logger library for putting data in JSON format into model.
        # ref: https://github.com/CiCiUi/django-db-logger
        
        db_logger.info("<TemperatureView>: Logging Details", { 
            "data": serialize('json', temperatures)
        })

        return render(request, 'temperature.html', {'temperatures': temperatures})
