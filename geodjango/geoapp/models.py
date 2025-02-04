from django.contrib.gis.db import models
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=250, default=' - ', blank=False, verbose_name='Название точек')
    location = models.PointField(srid=4326, verbose_name='Местонахождение точки')

    class Meta:
        verbose_name = 'Импорт точек маршрута'
        verbose_name_plural = 'Импорт точек маршрута'


    def __str__(self):
        return self.name
