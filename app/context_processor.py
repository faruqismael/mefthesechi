from . import models
from .forms import VisaStatusCheckForm
from django.shortcuts import get_object_or_404


def local(request):
    settings = models.WebsiteSetting.objects.first()
    about_data = models.About.objects.prefetch_related("images").first()
    carousel_slides = models.CarouselSlide.objects.filter(is_active=True)
    destinations = models.Destination.objects.all()
    services = models.Service.objects.prefetch_related("features").all()
    galleries = models.GalleryImage.objects.all()
    facts = models.Fact.objects.all()

    return {
        "settings": settings,
        "about_data": about_data,
        "carousel_slides": carousel_slides,
        "destinations": destinations,
        "services": services,
        "galleries": galleries,
        "facts": facts,
    }
