from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers import RestautantSerializer
from .models import Restaurant


class RestaurantListAPIView(APIView):
    # queryset = Restaurant.objects.all()
    # serializer_class = RestautantSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def get(self, request):
        queryset = Restaurant.objects.all()
        return Response({'restaurants': queryset})
    