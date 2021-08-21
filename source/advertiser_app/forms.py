from django import forms
from advertiser_app.models import (
    Advert,
    Status,
    Category
)


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")


class AdvertForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Advert
        fields = ('title', 'description', 'price', 'image', 'category')