from django.db import models

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    price_month = models.CharField(max_length=10, default='N/A')
    shorter_info = models.TextField(default='N/A')
    short_info = models.TextField(default='short info')
    traction = models.TextField(default='N/A')
    gearbox = models.TextField(default='Automatic')
    engine = models.TextField(default='N/A')
    stock = models.TextField(default='N/A')
    vin = models.TextField(default='N/A')
    mileage = models.TextField(default='N/A')
    body_color = models.TextField(default='N/A')
    interior_color = models.TextField(default='N/A')
    year = models.IntegerField()
    photo_test_main = models.TextField(default='N/A')
    video_photo = models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1024px-YouTube_full-color_icon_%282017%29.svg.png')
    video_link = models.TextField(default='<iframe width="1029" height="579" src="https://www.youtube.com/embed/BcJN9JGaYFQ" title="1977 CHEVROLET K20" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Price: {self.price}, Mileage: {self.mileage}, Color: {self.body_color}, Interior: {self.interior_color}, VIN: {self.vin}"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo1 = models.TextField(default='https://cdn.dealeraccelerate.com/worldwide/1/8226/510832/1920x1440/w/1986-mercedes-benz-560sl')

# Create your models here.
