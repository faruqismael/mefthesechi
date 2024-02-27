from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import Vacancy


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


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
