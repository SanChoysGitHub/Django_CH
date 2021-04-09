from django import forms
from .models import Category


class NewsForm(forms.Form):




    #--------------------------------------------------------------------------------------
    # ФОРМА НЕСВЯЗАННАЯ С МОДЕЛЬЮ
    # title = forms.CharField(max_length=150, label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
    #     "class": "form-control",
    #     "rows": 5,
    # }))
    # is_published = forms.BooleanField(label='Published?', initial=True)
    # category = forms.ModelChoiceField(empty_label='Choose category', label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    # --------------------------------------------------------------------------------------
