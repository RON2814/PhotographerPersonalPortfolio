from django import forms
from backend.models import PortfolioProject

class PortfolioProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['title', 'image', 'description']
