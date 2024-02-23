from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _

# This changes the site header
admin.site.site_header = _("Mefthesechi Agency Admin")

# This changes the site title
admin.site.site_title = _("Mefthesechi Agency Admin Interface")

# Optional: Change the index title
admin.site.index_title = _("Welcome to Mefthesechi Agency Admin")


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")
    list_filter = ("date_added",)
    search_fields = ("title", "description")


@admin.register(models.WebsiteSetting)
class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ["site_name", "email", "phone_number"]


# Register your models here.
@admin.register(models.CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "button_text")


@admin.register(models.Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "link")


class ServiceFeatureInline(admin.TabularInline):
    model = models.ServiceFeature
    extra = 1


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")
    inlines = [ServiceFeatureInline]


@admin.register(models.Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("title", "number")


admin.site.register(models.About)
admin.site.register(models.AboutImage)
admin.site.register(models.Profession)
admin.site.register(models.JobApplication)
admin.site.register(models.GalleryImage, GalleryImageAdmin)
