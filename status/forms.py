from .models import Status
from django import forms

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'image',
            'content',
        ]

    def clean_content(self):
        print('#####################333')
        content = self. cleaned_data.get('content')
        if len(content) > 240:
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$44')
            raise forms.ValidationError("content is too long")
        return content

    def clean(self):
        data = self.cleaned_data
        content = data.get('content') or None
        image = data.get('image') or None
        if content is None and image is None:
            raise forms.ValidationError("Content or image is required")
        return super().clean()

