from django.db import models


class Sensor(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Название датчика'
        )
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'Датчик: ID={self.id}, Название: {self.name}'
    

class Measurement(models.Model):
    sensor_id = models.ForeignKey(
        Sensor, 
        on_delete=models.CASCADE, 
        related_name='measurements'
        )
    temperature = models.DecimalField(
        decimal_places=1, 
        max_digits=3, 
        verbose_name='Температура'
        )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Время и дата измерения'
        )
    photo = models.ImageField(upload_to = 'media', null=True, blank=True)
    class Meta:
        verbose_name = 'Измерение температуры'
        verbose_name_plural = 'Измерения температуры'
    
    def __str__(self):
        return f'Измение от {self.created}, датчик: {self.sensor_id}, температура: {self.temperature}'