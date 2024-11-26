from django import forms
from .models import VlogPost

class VlogPostForm(forms.ModelForm):
    class Meta:
        model = VlogPost
        fields = ['title', 'video_url', 'description', 'tags']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_video_url(self):
        video_url = self.cleaned_data.get('video_url')
        if not video_url.startswith("http"):
            raise forms.ValidationError("Invalid URL format. Must start with http or https.")
        return video_url

    def clean_description(self):
        title = self.cleaned_data.get('description')
        if len(title) < 20:
            raise forms.ValidationError("Description must be at least 20 characters long.")
        return title