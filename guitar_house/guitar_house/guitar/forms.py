from django import forms

from guitar_house.guitar.models import Guitar




class GuitarBasicForm(forms.ModelForm):
    user = None
    class Meta:
        model = Guitar
        fields = ['brand', 'model', 'type', 'price', 'image_url', 'description', 'short_description']
class GuitarCreationForm(GuitarBasicForm):
    pass




class GuitarEditForm(GuitarBasicForm):
    read_only_fields = ('type',)


