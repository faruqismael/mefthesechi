from . import models


def local(request):
    settings = (
        models.WebsiteSetting.objects.first()
    )  # Assuming you have only one entry.
    about_data = models.About.objects.prefetch_related(
        "images"
    ).first()  # Assuming there's only one About instance
    carousel_slides = models.CarouselSlide.objects.filter(is_active=True)
    destinations = models.Destination.objects.all()
    services = models.Service.objects.prefetch_related("features").all()
    facts = models.Fact.objects.all()

    return {
        "settings": settings,
        "about_data": about_data,
        "carousel_slides": carousel_slides,
        "destinations": destinations,
        "services": services,
        "facts": facts,
    }
