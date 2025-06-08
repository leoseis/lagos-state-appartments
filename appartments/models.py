from django.db import models

# Create your models here.


class Appartment(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image =  models.ImageField(upload_to='item', blank=True, null=True)




    def __str__(self):
        return self.title
