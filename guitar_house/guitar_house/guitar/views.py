from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from guitar_house.guitar.forms import GuitarEditForm
from guitar_house.guitar.models import Guitar

UserModel = get_user_model()
class MakeFieldsReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = 'readonly'

class ContextDataMixin:

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                profile = Guitar.objects.first()
                context['profile'] = profile
                return context




# Create your views here.
class DetailGuitarView(views.DetailView):
    queryset = Guitar.objects.all()
    template_name = 'guitars/guitar-info.html'




class CreateGuitarView(LoginRequiredMixin, views.CreateView):
    queryset = Guitar.objects.all()
    fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
    template_name = 'guitars/add-guitar.html'

    success_url = reverse_lazy('guitars')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditGuitarView(ContextDataMixin,views.UpdateView):
    model = Guitar
    form_class = GuitarEditForm
    template_name = 'guitars/edit-guitar.html'

    success_url = reverse_lazy('guitars')



class ReviewGuitarsView(views.DetailView):
    queryset = Guitar.objects.all()
    context_object_name = 'guitar'
    template_name = 'guitars/review.html'





