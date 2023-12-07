from django import forms
from .models import Bug

class BugUpdateForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'status', 'project', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
