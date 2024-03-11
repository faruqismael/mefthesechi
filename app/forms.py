from django import forms
from .models import JobApplication, Destination


class JobApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)

        # Dynamically load desired_country choices from Destination model

        self.fields["sex"].widget.attrs.update({"class": "form-control"})
        self.fields["region"].widget.attrs.update({"class": "form-control"})
        self.fields["desired_country"].widget.attrs.update({"class": "form-control"})

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
