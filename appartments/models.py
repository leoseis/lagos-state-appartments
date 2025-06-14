from django.db import models

# Create your models here.

# models.py
class Agent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Appartment(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='appartments/covers/', blank=True, null=True) 
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
 # main image

    def __str__(self):
        return self.title

class ApartmentImage(models.Model):
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ImageField(upload_to='appartments/gallery/')

    def __str__(self):
        return f"Image for {self.appartment.title}"


    # def __str__(self):
        # return self.title
