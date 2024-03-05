from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from guitar_house.guitar.models import Guitar


# Create your views here.
class DetailGuitarView(views.DetailView):
    queryset = Guitar.objects.all()
    template_name = 'guitars/guitar-info.html'


class CreateGuitarView(views.CreateView):
    queryset = Guitar.objects.all()
    fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
    template_name = 'guitars/add-guitar.html'

    success_url = reverse_lazy('guitars')

class ShowGuitarsView(views.ListView):
    queryset = Guitar.objects.all().order_by('model')
    template_name = 'guitars/review.html'
    context_object_name = 'guitars'
    paginate_by = 3