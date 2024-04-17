from django.db import models
from django.urls import reverse

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)  
    description = models.TextField(max_length=250)
    age = models.IntegerField(default=0) 
    toys = models.ManyToManyField('Toy', blank=True)

    def __str__(self):
        return f'{self.name} ({self.breed}) - Age: {self.age}'

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'pk': self.pk}) 


class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.pk})
        
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=100)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings') 

    def __str__(self):
        return f"{self.meal} on {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-date']  
