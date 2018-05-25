from django import forms
from django.contrib.auth.models import User

from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['title', 'description', 'image_url', 'ask', 'category', 'created_at', 'closes']