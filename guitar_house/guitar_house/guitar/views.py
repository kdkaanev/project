from django.shortcuts import render
from django.views import generic as views

from guitar_house.guitar.models import Guitar


# Create your views here.
class DetailGuitarView(views.DetailView):
    queryset = Guitar.objects.all()
    template_name = 'guitars/guitar-info.html'
