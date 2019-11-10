from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    name = models.CharField('Название', max_length=40)
    location = models.PointField(srid=4326)
    comment = models.TextField('Комментарий о месте')
    author = models.ForeignKey(User, default=1, verbose_name='пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name