
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
 


class blogs (models.Model):
    title = models.CharField(max_length=50)
    image = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return self.title
    

class feedback (models.Model):
    name = models.CharField(max_length=50)
    
    suggestion = models.TextField()
    mail_id =models.EmailField()

    def __str__(self):
        return self.name


class profile_photo(models.Model):
    name = models.CharField(max_length=150)
    photo = CloudinaryField('image')
