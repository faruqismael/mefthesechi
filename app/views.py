from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import JobApplicationForm, ContactForm
from .models import Vacancy, VisaStatus
from .forms import VisaStatusCheckForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from django.views.generic import TemplateView, FormView


# class SuccessView(TemplateView):
#     template_name = "success.html"


# class ContactView(FormView):
#     form_class = ContactForm
#     template_name = "contact.html"

#     def get_success_url(self):
#         return reverse("contact")

#     def form_valid(self, form):
#         email = form.cleaned_data.get("email")
#         subject = form.cleaned_data.get("subject")
#         message = form.cleaned_data.get("message")

#         full_message = f"""
#             Received message below from {email}, {subject}
#             ________________________


#             {message}
#             """
#         send_mail(
#             subject="Received contact form submission",
#             message=full_message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.NOTIFY_EMAIL],
#         )
#         return super(ContactView, self).form_valid(form)


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            subject = request.POST["subject"]
            message = request.POST["message"]
            email_from = request.POST["email"]
            recipient_list = [settings.EMAIL_HOST_USER]

            try:
                send_mail(
                    subject + " - " + name,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
                return redirect("emailsuccess")  # Redirect to the 'success' URL
            except Exception as e:
                messages.error(request, f"Sorry, Can you please try later")
        else:
            messages.error(
                request, "There was an error in your form. Please check your input."
            )

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by("-posted_on")
    return render(request, "vacancy_list.html", {"vacancies": vacancies})


def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")  # Redirect to a 'thank you' page
    else:
        form = JobApplicationForm()
    return render(request, "apply.html", {"form": form})


def success(request):
    return render(request, "success.html")


def check_visa_status(request):
    if request.method == "POST":
        form = VisaStatusCheckForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data["id_number"]
            try:
                visa_status = VisaStatus.objects.get(id_number=id_number)
            except VisaStatus.DoesNotExist:
                message = "No visa status found for the provided ID."
                return render(request, "no_visa_status.html", {"message": message})
            return render(
                request, "visa_status_result.html", {"visa_status": visa_status}
            )
    else:
        form = VisaStatusCheckForm()

    return render(request, "check_visa_status.html", {"form": form})


def emailsuccess(request):
    return render(
        request,
        "emailsuccess.html",
        {"message": "Thank you for your message. We will get back to you shortly."},
    )
