from django.shortcuts import render, redirect
from .forms import JobApplicationForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    return render(request, "contact.html")


def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("apply")  # Redirect to a 'thank you' page
    else:
        form = JobApplicationForm()
    return render(request, "apply.html", {"form": form})
