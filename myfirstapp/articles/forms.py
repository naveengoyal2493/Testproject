from django import forms
from . import models

class CreateArticle(forms.ModelForms):
    class Meta:
        model = models.Article
        fields = ['title','slug','body','thumb']
