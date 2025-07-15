from django.db import models
from django.utils import timezone

# Create your models here.
class talkie_user_models(models.Model):
    subscription_type = [
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_time = models.DateTimeField(default=timezone.now)
    type =  models.CharField(max_length=20, choices=subscription_type)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)

    def __str__(self):
        return self.name