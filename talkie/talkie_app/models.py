from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    duration = models.CharField(max_length=50, default='')
    exe_file = models.FileField(upload_to='executables/', null=True, blank=True)

    def __str__(self):
        return self.name
    
# one to many relationship with talkie_user_models

class talkie_review(models.Model):
    talkie_plan_review = models.ForeignKey(talkie_user_models, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(default='')
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # return f"{self.user.username} - {self.talkie_plan_review.name} - {self.rating}"
        return f"{self.user.username} review for {self.talkie_plan_review.name} - {self.rating} stars"
    
# many to many relationship with talkie_user_models

class talkie_favourite(models.Model):
    talkie_plan_favourite = models.ManyToManyField(talkie_user_models, related_name='favourites')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} favourites"

#one to one relationship with talkie_user_models
class talkie_user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    talkie_plan = models.ForeignKey(talkie_user_models, on_delete=models.SET_NULL, null=True, blank=True)
    profile_created_data_time = models.DateTimeField(auto_now_add=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} profile"