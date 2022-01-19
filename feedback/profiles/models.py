from django.db import models


# Create your models here.


class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")  # file will not be stored in a database, instead on a local hardrive and store path
