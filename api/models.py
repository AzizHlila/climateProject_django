from django.db import models
    
class Factors(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=1000)

class Chart(models.Model):
    climate_paramter = models.ForeignKey(Factors,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="user_images", default="default.jpg")


class Solutions(models.Model):
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=1000,)
    date = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to="user_images", default="default.jpg")


class Information(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    is_true = models.BooleanField(default=True)


