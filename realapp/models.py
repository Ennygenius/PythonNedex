from django.db import models

# Create your models here.
class Housing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=250,unique=True)
    price = models.FloatField(unique=True)
    decription = models.TextField(unique=True)
    num_of_bedrooms = models.IntegerField()
    image = models.ImageField(upload_to="images/", default=True, unique=True)


    def __str__(self):
        return self.location
    