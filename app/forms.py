from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["full_name", "profession", "email", "documents", "coc", "photos"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your full name"}
            ),
            "profession": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "yourname@example.com"}
            ),
            # Customize other fields similarly
        }
