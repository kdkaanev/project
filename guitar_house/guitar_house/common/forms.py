from django import forms

from guitar_house.common.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
