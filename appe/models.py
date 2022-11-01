from django.db import models

# Create your models here.

class Images(models.Model):
    image_name=models.CharField(max_length=150,null=True)
    image=models.ImageField(upload_to='image')
    def __str__(self):
        return self.image_name
