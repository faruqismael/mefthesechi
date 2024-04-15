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
    path("emailsuccess  ", views.emailsuccess, name="emailsuccess "),
    path("vacancy", views.vacancy_list, name="vacancy"),
    path("check_visa_status", views.check_visa_status, name="check_visa_status"),
]
