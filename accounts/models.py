from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profileModel(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Name = models.CharField(max_length = 100)
    # Family = models.CharField(max_length = 100)
    ProfileImage = models.ImageField(upload_to="profileImages/", blank=True, default="static/accounts/images/user-icon2.png")
    Email = models.EmailField()

    Man=1
    Woman=2
    Other=3
    Status_choices = ((Man, "Man"), (Woman, "Woman"), (Other, "Other"))
    Gender = models.IntegerField(choices = Status_choices, null = True)

