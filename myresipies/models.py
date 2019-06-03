from django.db import models

# Create your models here

class Resepi(models.Model):
    name  = models.CharField(max_length=20)
    ingredients= models.TextField()
    process = models.TextField(null=True,blank=True)
    image = models.URLField(null= True, blank= True,)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name



