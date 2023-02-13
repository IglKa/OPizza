from django.urls import path

from .views import *
from .API import *


app_name = 'restaurant'

urlpatterns = [
    # Restaurant views for site
    path('', RestaurantView.as_view(), name='restr'),

    # API views
    path('api/v1/', RestaurantListAPIView.as_view()),
]
