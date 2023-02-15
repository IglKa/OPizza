from django.views.generic import ListView, DetailView

from restaurant.models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    context_object_name = 'rstr'
    template_name = 'base.html'


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'
    context_object_name = 'rstr'

    # def get(self, request, *args, **kwargs):
    #     meals = find_meals()
