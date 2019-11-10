from django.contrib.gis.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField('Название', max_length=40)
    location = models.PointField(srid=4326)
    comment = models.TextField('Комментарий о месте')