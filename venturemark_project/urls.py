from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('https://ised-isde.canada.ca/cipo/trademark-search/srch?lang=eng', views.check_trademark, name='check-trademark'),
]
