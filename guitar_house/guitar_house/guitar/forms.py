from django import forms

from guitar_house.guitar.models import Guitar, Review


class GuitarBasicForm(forms.ModelForm):
    user = None
    class Meta:
        model = Guitar
        fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
class GuitarCreationForm(GuitarBasicForm):
    pass




class GuitarEditForm(GuitarBasicForm):
   pass




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']


