from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City

class Train(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Name of train')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                #   null=True, blank=True,
                                  related_name='from_city_set',
                                  verbose_name='From'
                                  )
    to_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                #   null=True, blank=True,
                                related_name='to_city_set',
                                verbose_name='To'
                               )
    

    def __str__(self):
        return f'Train # {self.name} from city : {self.from_city}'
    

    class Meta:
        verbose_name = "Train"
        verbose_name_plural = "Trains"
        ordering = ['from_city']  # сортируем по городу отправления

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Please, change arrival city!!!')
        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        # Train == self.__class__
        if qs.exists():
            raise ValidationError('Please, change travel time!!!')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    