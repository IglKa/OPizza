from django.urls import path

from .views import *
from .API import *


app_name = 'restaurant'

urlpatterns = [
    # Restaurant views for site
    path('', RestaurantListView.as_view(), name='restr'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restr-detail'),

    # API views
    path('api/v1/', RestaurantListAPIView.as_view()),
]
