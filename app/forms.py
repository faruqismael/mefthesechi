from django import forms
from .models import JobApplication, Destination, VisaStatus


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


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )


class VisaStatusCheckForm(forms.Form):
    id_number = forms.CharField(max_length=255, label="ID Number")
    # def clean_id_number(self):
    #     id_number = self.cleaned_data.get("id_number")
    #     try:
    #         visa_status = VisaStatus.objects.get(id_number=id_number)
    #     except VisaStatus.DoesNotExist:
    #         raise forms.ValidationError("Invalid ID number.")
    #     return visa_status
