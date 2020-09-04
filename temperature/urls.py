
from temperature.views import TemperatureView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', TemperatureView.as_view(), name='temperatureview'),
]