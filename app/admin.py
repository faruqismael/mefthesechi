from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django import forms

# This changes the site header
admin.site.site_header = _("Mefthesechi Agency Admin")

# This changes the site title
admin.site.site_title = _("Mefthesechi Agency Admin Interface")

# Optional: Change the index title
admin.site.index_title = _("Welcome to Mefthesechi Agency Admin")


class VacancyAdminForm(forms.ModelForm):
    class Meta:
        model = models.Vacancy
        widgets = {"description": CKEditorWidget()}
        fields = "__all__"


class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm


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


@admin.register(models.VisaStatus)
class VisaStatusAdmin(admin.ModelAdmin):
    list_display = ("job_application", "status")
    list_filter = ("status",)
    search_fields = (
        "job_application__full_name",
        "job_application__phone_number",
    )  # Adjust based on your model fields


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
admin.site.register(models.Vacancy, VacancyAdmin)
