from django import forms
from .models import Exercise

MAX_TWEET_LENGTH = 240

class SearchForm(forms.ModelForm):
    search = forms.CharField()
    class Meta:
        model = Exercise
        fields = ['search']

    def clean_search(self):
        search = self.cleaned_data.get("search")
        if len(search) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return search