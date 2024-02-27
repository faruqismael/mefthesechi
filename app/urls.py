from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("gallery", views.gallery, name="gallery"),
    path("contact", views.contact, name="contact"),
    path("apply", views.apply, name="apply"),
    path("success", views.success, name="success"),
    path("vacancy", views.vacancy_list, name="vacancy"),
]
