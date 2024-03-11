from django.db import models

from ckeditor.fields import RichTextField


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=100, help_text="The name of the website.")
    logo = models.ImageField(
        upload_to="logos/", blank=True, null=True, help_text="Logo of the website."
    )
    facebook_url = models.URLField(
        blank=True, null=True, help_text="Facebook page URL."
    )
    twitter_url = models.URLField(
        blank=True, null=True, help_text="Twitter profile URL."
    )
    linkedin_url = models.URLField(
        blank=True, null=True, help_text="LinkedIn profile URL."
    )
    instagram_url = models.URLField(
        blank=True, null=True, help_text="Instagram profile URL."
    )
    youtube_url = models.URLField(
        blank=True, null=True, help_text="YouTube channel URL."
    )
    email = models.EmailField(help_text="Contact email address.")
    phone_number = models.CharField(max_length=20, help_text="Contact phone number.")
    address = models.TextField(blank=True, null=True, help_text="Physical address.")
    copyright_text = models.TextField(
        blank=True, null=True, help_text="Copyright text for the footer."
    )
    about_us_text = models.TextField(
        blank=True,
        null=True,
        help_text="Short description about the website or company for the footer.",
    )
    google_map_iframe = models.TextField(
        blank=True, null=True, help_text="Google Map iframe code for the contact page."
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Website Setting"
        verbose_name_plural = "Website Settings"


class CarouselSlide(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField()
    button_text = models.CharField(max_length=50, default="Contact Us")
    button_link = models.CharField(max_length=255, default="/contact")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# about
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Additional fields as necessary

    def __str__(self):
        return self.title


class AboutImage(models.Model):
    about = models.ForeignKey(About, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField()
    alt_text = models.CharField(
        max_length=255, blank=True, help_text="Alternative text for image"
    )

    def __str__(self):
        return f"Image for {self.about.title} - {self.alt_text}"


class Destination(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="destinations/")
    description = models.TextField(blank=True, null=True)  # Optional description field
    link = models.URLField(blank=True, null=True)  # Optional link field

    def __str__(self):
        return self.name


# services
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(
        max_length=255, help_text="FontAwesome icon class, e.g., 'fa-users'"
    )
    description = models.TextField(
        blank=True, help_text="Brief description of the service."
    )

    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(
        Service, related_name="features", on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=255, help_text="Specific feature or step in the service."
    )

    def __str__(self):
        return f"{self.service.title} - {self.text}"


class Fact(models.Model):
    icon_class = models.CharField(
        max_length=255, help_text="FontAwesome icon class, e.g., 'fa-users'"
    )
    title = models.CharField(max_length=255)
    number = models.CharField(
        max_length=255,
        blank=True,
        help_text="Number to display with a '+' sign if needed.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description for countries or additional info.",
    )

    def __str__(self):
        return self.title


# apply
class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    SEX_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    REGION_CHOICES = [
        ("addis_ababa", "Addis Ababa"),
        ("oromia", "Oromia"),
        ("amhara", "Amhara"),
        ("tigray", "Tigray"),
        ("south", "South"),
        ("somali", "Somali"),
        ("afar", "Afar"),
        ("benishangul", "Benishangul Gumuz"),
        ("gambella", "Gambella"),
        ("harar", "Harar"),
        # Add more regions as needed.
    ]

    DESIRED_COUNTRY_CHOICES = [
        ("jordan", "Jordan"),
        ("saudi_arabia", "Saudi Arabia"),
        ("dubai", "Dubai"),
        ("qatar", "Qatar"),
    ]

    full_name = models.CharField(max_length=255)
    passport = models.FileField(blank=True, upload_to="passports/")
    sex = models.CharField(blank=True, max_length=6, choices=SEX_CHOICES)
    region = models.CharField(
        default="Addis Ababa", max_length=50, choices=REGION_CHOICES
    )
    phone_number = models.CharField(blank=True, max_length=20)
    desired_country = models.CharField(
        blank=True, max_length=50, choices=DESIRED_COUNTRY_CHOICES
    )

    def __str__(self):
        return f"{self.full_name} - {self.desired_country}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the image")
    description = models.TextField(
        blank=True, help_text="A brief description of the image"
    )
    image = models.ImageField(
        upload_to="gallery_images/", help_text="Upload the gallery image here"
    )
    date_added = models.DateTimeField(
        auto_now_add=True, help_text="The date and time this image was added"
    )

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
