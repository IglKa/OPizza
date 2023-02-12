from django.urls import path
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('api/v1/', RestaurantListAPIView.as_view())
]