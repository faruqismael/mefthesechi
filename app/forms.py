from django import forms
from .models import JobApplication, Destination


class JobApplicationForm(forms.ModelForm):
    SEX_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    REGION_CHOICES = [
        ("addis_ababa", "Addis Ababa"),
        ("oromia", "Oromia"),
        ("amhara", "Amhara"),
        ("tigray", "Tigray"),
        # Add more as needed
    ]

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        # Dynamically load desired_country choices from Destination model
        self.fields["desired_country"] = forms.ModelChoiceField(
            queryset=Destination.objects.all(),
            widget=forms.Select(attrs={"class": "form-control"}),
            required=True,
        )
        self.fields["sex"].widget.attrs.update({"class": "form-control"})
        self.fields["region"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = JobApplication
        fields = [
            "full_name",
            "passport",
            "sex",
            "region",
            "phone_number",
            "desired_country",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your full name"}
            ),
            "passport": forms.FileInput(attrs={"class": "form-control-file"}),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
        }
