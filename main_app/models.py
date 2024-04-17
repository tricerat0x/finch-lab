from django.db import models
from django.urls import reverse

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)  # Optional, based on second model
    description = models.TextField(max_length=250)
    age = models.IntegerField(default=0)  # Added default as age might not always be provided

    def __str__(self):
        return f'{self.name} ({self.breed}) - Age: {self.age}'

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'pk': self.pk})  # Unified URL name

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=100)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings')  # Added related_name for reverse access

    def __str__(self):
        return f"{self.meal} on {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-date']  # Orders feedings by date, latest first
