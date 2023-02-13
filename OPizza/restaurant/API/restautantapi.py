from rest_framework.generics import ListAPIView

from .serializers import RestautantSerializer
from restaurant.models import Restaurant


class RestaurantListAPIView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestautantSerializer
    