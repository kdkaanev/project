from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import messages

from guitar_house.guitar.forms import GuitarEditForm, ReviewForm
from guitar_house.guitar.models import Guitar, Review

UserModel = get_user_model()
class MakeFieldsReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = 'readonly'






# Create your views here.
class DetailGuitarView(views.DetailView):
    queryset = Guitar.objects.all()
    template_name = 'guitars/guitar-info.html'




class CreateGuitarView(LoginRequiredMixin, views.CreateView):
    queryset = Guitar.objects.all()
    fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
    template_name = 'guitars/add-guitar.html'

    success_url = reverse_lazy('user-guitars')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditGuitarView(views.UpdateView):
    queryset = Guitar.objects.all()
    fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
    template_name = 'guitars/edit-guitar.html'

    success_url = reverse_lazy('user-guitars')



class ReviewGuitarsView(views.DetailView):


    queryset = Guitar.objects.all()
    context_object_name = 'guitar'
    template_name = 'guitars/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guitar = self.get_object()
        context['reviews'] = guitar.review_set.all()
        return context









class DeleteGuitarView(views.DeleteView):
    queryset = Guitar.objects.all()
    template_name = 'guitars/delete-guitar.html'
    success_url = reverse_lazy('user-guitars')




def add_review(request, guitar_id):
    if not request.user.is_authenticated:
        messages.error(request, "Only logged in users can make a review.")
        return redirect('sign-in')
    else:
        guitar = get_object_or_404(Guitar, pk=guitar_id)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.guitar = guitar
                review.user = request.user
                review.save()
                return redirect('guitar-reviews', guitar.pk)
        else:
            form = ReviewForm()
    return render(request, 'guitars/write-review.html', {'form': form})





