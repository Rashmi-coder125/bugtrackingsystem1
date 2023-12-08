from django import forms
from .models import Bug
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BugUpdateForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'status', 'project', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('Open', 'Open'), ('InProgress', 'InProgress'), ('Closed', 'Closed')]),
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
