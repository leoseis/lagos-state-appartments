from django.db import models

# Create your models here.

# models.py
from django.db import models

class Appartment(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='appartments/covers/', blank=True, null=True)  # main image

    def __str__(self):
        return self.title

class ApartmentImage(models.Model):
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ImageField(upload_to='appartments/gallery/')

    def __str__(self):
        return f"Image for {self.appartment.title}"


    # def __str__(self):
        # return self.title
