from django.views.generic import ListView

from restaurant.models import Restaurant


class RestaurantView(ListView):
    model = Restaurant
    context_object_name = 'rstr'
    template_name = 'base.html'
